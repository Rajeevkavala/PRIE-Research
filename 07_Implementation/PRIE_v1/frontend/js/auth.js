/**
 * PRIE v1 — Authentication & Session Manager
 * File: frontend/js/auth.js
 */

const AuthManager = (() => {
  function checkSession(requireAdmin = false) {
    if (!Auth.isLoggedIn()) {
      // Determine relative path to login.html
      const currentPath = window.location.pathname;
      const target = currentPath.includes('/pages/') ? 'login.html' : 'pages/login.html';
      window.location.href = target;
      return false;
    }
    if (requireAdmin && !Auth.isAdmin()) {
      showToast('Admin privilege required for this view.', 'warning');
      const target = window.location.pathname.includes('/pages/') ? 'dashboard.html' : 'pages/dashboard.html';
      window.location.href = target;
      return false;
    }
    return true;
  }

  function initHeaderUser() {
    const nameEl = document.getElementById('user-name');
    const avatarEl = document.getElementById('avatar-initials');
    if (nameEl) nameEl.textContent = Auth.getName();
    if (avatarEl) avatarEl.textContent = Auth.getInitials();

    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
      logoutBtn.addEventListener('click', () => {
        Auth.clear();
        showToast('Logged out successfully', 'info');
        setTimeout(() => {
          const target = window.location.pathname.includes('/pages/') ? 'login.html' : 'pages/login.html';
          window.location.href = target;
        }, 500);
      });
    }
  }

  return {
    checkSession,
    initHeaderUser,
    logout: () => {
      Auth.clear();
      const target = window.location.pathname.includes('/pages/') ? 'login.html' : 'pages/login.html';
      window.location.href = target;
    }
  };
})();

// Auto-run header init if DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  if (Auth.isLoggedIn()) {
    AuthManager.initHeaderUser();
  }
});
