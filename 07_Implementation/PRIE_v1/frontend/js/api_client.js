/**
 * PRIE v1 — REST API Client
 * File: frontend/js/api_client.js
 */

const API_BASE = 'http://127.0.0.1:8000/api/v1';

const ApiClient = (() => {
  function _headers() {
    const token = localStorage.getItem('prie_token');
    return {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    };
  }

  async function _request(method, path, body = null) {
    const opts = { method, headers: _headers() };
    if (body) opts.body = JSON.stringify(body);
    try {
      const res = await fetch(`${API_BASE}${path}`, opts);
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || `HTTP ${res.status}`);
      return data;
    } catch (e) {
      console.error(`[PRIE API] ${method} ${path}:`, e.message);
      throw e;
    }
  }

  return {
    // Auth
    register: (payload) => _request('POST', '/auth/register', payload),
    login:    (payload) => _request('POST', '/auth/login', payload),

    // Profile
    getProfile: () => _request('GET', '/profile/me'),
    getSPV:     () => _request('GET', '/profile/spv'),
    updateProfile: (payload) => _request('PUT', '/profile/update', payload),

    // Prediction
    predictReadiness: () => _request('POST', '/predict/readiness'),

    // XAI
    prescribe: () => _request('POST', '/explain/prescribe'),

    // Roadmap
    getRoadmap:      () => _request('GET', '/roadmap/active'),
    generateRoadmap: () => _request('POST', '/roadmap/generate'),
    completeWeek:    (week) => _request('POST', `/roadmap/complete/${week}`),

    // Assessment
    getTopics:   () => _request('GET', '/assessment/topics'),
    nextQuestion: (topic, history) => _request('POST', `/assessment/next-item/${topic}`, { history }),
    submitAnswer: (payload) => _request('POST', '/assessment/submit', payload),
    getMastery:  (topic) => _request('GET', `/assessment/mastery/${topic}`),

    // Resume Intelligence & ATS (M02)
    analyzeResumeText: (text, targetRole = 'Software Development Engineer') =>
      _request('POST', '/resume/analyze-text', { resume_text: text, target_role: targetRole }),
    uploadResumePdf: async (formData) => {
      const token = localStorage.getItem('prie_token');
      const res = await fetch(`${API_BASE}/resume/upload-pdf`, {
        method: 'POST',
        headers: token ? { Authorization: `Bearer ${token}` } : {},
        body: formData,
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || `HTTP ${res.status}`);
      return data;
    },

    // Multimodal Mock Interview Coach (M05)
    analyzeInterviewText: (transcript, durationSec = 60) =>
      _request('POST', '/interview/analyze-text', { transcript, duration_seconds: durationSec }),
    uploadInterviewMedia: async (formData) => {
      const token = localStorage.getItem('prie_token');
      const res = await fetch(`${API_BASE}/interview/analyze-media`, {
        method: 'POST',
        headers: token ? { Authorization: `Bearer ${token}` } : {},
        body: formData,
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || `HTTP ${res.status}`);
      return data;
    },

    // RAG Curriculum Assistant (M09)
    queryRAG: (query, topK = 3) =>
      _request('POST', '/rag/query', { query, top_k: topK }),

    // Bloom's Automated Question Generation (M10)
    generateAQG: (topic, difficulty = 'Medium', bloomLevel = 'Apply', count = 3) =>
      _request('POST', '/aqg/generate', { topic, difficulty, bloom_level: bloomLevel, count }),

    // Company Benchmark Matcher (M11)
    getCompanies: () => _request('GET', '/company/benchmarks'),
    matchCompany: (spvVector = null) =>
      _request('POST', '/company/match', { spv_vector: spvVector }),

    // Digital Twin What-If Recourse (M12)
    simulateWhatIf: (deltas, spvVector = null) =>
      _request('POST', '/twin/what-if', { feature_deltas: deltas, base_spv_vector: spvVector }),
    getSensitivity: (spvVector = null) =>
      _request('POST', '/twin/sensitivity', { spv_vector: spvVector }),

    // Experiment Runner & Results (EXP-1 to EXP-6)
    getExperiments: () => _request('GET', '/experiments/'),
    getExperimentDetails: (expId) => _request('GET', `/experiments/${expId}`),
  };
})();

// Auth state helpers
const Auth = {
  save(data) {
    localStorage.setItem('prie_token', data.access_token);
    localStorage.setItem('prie_student_id', data.student_id);
    localStorage.setItem('prie_name', data.name || '');
    localStorage.setItem('prie_is_admin', data.is_admin || false);
  },
  clear() {
    ['prie_token','prie_student_id','prie_name','prie_is_admin'].forEach(k => localStorage.removeItem(k));
  },
  isLoggedIn() { return !!localStorage.getItem('prie_token'); },
  getName()    { return localStorage.getItem('prie_name') || 'Student'; },
  isAdmin()    { return localStorage.getItem('prie_is_admin') === 'true'; },
  getInitials() {
    const n = this.getName();
    return n.split(' ').map(w => w[0]).join('').toUpperCase().slice(0,2) || 'U';
  },
  requireAuth() {
    if (!this.isLoggedIn()) { window.location.href = '/login.html'; return false; }
    return true;
  },
};

// Toast notification
function showToast(msg, type = 'info') {
  let t = document.getElementById('prie-toast');
  if (!t) {
    t = document.createElement('div');
    t.id = 'prie-toast';
    t.style.cssText = `
      position:fixed;bottom:24px;right:24px;z-index:9999;
      padding:12px 20px;border-radius:12px;font-size:0.875rem;font-weight:600;
      font-family:'Inter',sans-serif;max-width:340px;
      box-shadow:0 8px 30px rgba(0,0,0,0.5);
      transition:all 0.3s cubic-bezier(0.4,0,0.2,1);
      transform:translateY(100px);opacity:0;
    `;
    document.body.appendChild(t);
  }
  const colors = {
    info:    'rgba(139,92,246,0.9)',
    success: 'rgba(34,197,94,0.9)',
    warning: 'rgba(245,158,11,0.9)',
    error:   'rgba(244,63,94,0.9)',
  };
  t.style.background = colors[type] || colors.info;
  t.style.color = '#fff';
  t.textContent = msg;
  t.style.transform = 'translateY(0)';
  t.style.opacity = '1';
  setTimeout(() => { t.style.transform = 'translateY(100px)'; t.style.opacity = '0'; }, 3500);
}
