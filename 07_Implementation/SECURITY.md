# PRIE SECURITY & COMPLIANCE SPECIFICATION
**System**: ScholarCamp / Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 07 — Research-Grade Implementation  
**Quality Protocol**: Section 39 & 44 Compliance

---

## 1. Authentication & Cryptographic Standards

### A. JWT Token Management
* **Algorithm**: HMAC-SHA256 (`HS256`).
* **Secret Key**: Loaded dynamically from `PRIE_JWT_SECRET` environment variable. In `production` and `research` environments, fallback to insecure default keys is blocked at startup.
* **Token Expiration**: Access tokens expire automatically after 8 hours (`ACCESS_TOKEN_EXPIRE_MINUTES = 480`).
* **Signature Verification**: Validated on every protected endpoint via the FastAPI dependency `get_current_student()`.

### B. Credential Storage
* **Algorithm**: `bcrypt` adaptive salted password hashing (`passlib.context.CryptContext(schemes=["bcrypt"], deprecated="auto")`).
* **Plaintext Prohibition**: Plaintext passwords are never stored in the database, serialized in JSON responses, or emitted in log files.

---

## 2. API & Network Security

### A. CORS Configuration
* Wildcard (`"*"`) origins are strictly prohibited in `research` and `production` modes.
* CORS origins are explicitly configured in `config.py` (`http://localhost:8000`, `http://127.0.0.1:8000`, `http://localhost:3000`).

### B. Rate Limiting & Input Validation
* All incoming JSON bodies are strictly validated against Pydantic v2 schemas.
* Out-of-bounds numbers, injection strings, unexpected fields, and corrupted tensors are rejected at the HTTP gateway before reaching research modules.

---

## 3. Secure File Upload & Media Processing

### A. Resume PDF Uploads (`/api/v1/resume/upload-pdf`)
1. **Size Limit**: Enforced maximum payload of 5 MB (`MAX_UPLOAD_SIZE_BYTES = 5 * 1024 * 1024`).
2. **MIME & Extension Validation**: Only valid PDF headers (`%PDF-`) and `.pdf` extensions are accepted. Executables, scripts, and archives are rejected.
3. **Path Traversal Prevention**: Filenames are sanitized via `Path(file.filename).name` before temporary storage, preventing directory traversal attacks (`../../`).

### B. Interview Media Uploads (`/api/v1/interview/analyze-media`)
1. **Size Limit**: Enforced maximum payload of 50 MB for recorded audiovisual webm streams.
2. **Temporary File Lifecycle**: Media files are processed in isolated temporary directories and automatically cleaned up post-analysis.

---

## 4. Observability & Privacy Protection

* **Structured Logging**: Emits JSON-compatible logs with `request_id`, `student_id`, `module`, and `execution_duration_ms`.
* **Redaction Rules**:
  - Passwords and JWT tokens are masked (`[REDACTED]`).
  - Private interview media files and verbatim audio streams are restricted from log output.
  - Exception handlers catch internal errors and return structured HTTP responses (`{"detail": "..."}`) without leaking internal file paths or server environment variables.
