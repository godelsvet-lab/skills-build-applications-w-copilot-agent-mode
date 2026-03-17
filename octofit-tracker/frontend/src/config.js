const codespace = process.env.REACT_APP_CODESPACE_NAME;
const protocol = codespace ? 'https' : 'http';
const host = codespace ? `${codespace}-8000.app.github.dev` : 'localhost:8000';

export const API_BASE_URL = `${protocol}://${host}/api`;

export function endpointFor(resource) {
  return `${API_BASE_URL}/${resource}/`;
}

export function normalizeApiListPayload(payload) {
  if (Array.isArray(payload)) {
    return payload;
  }

  if (payload && Array.isArray(payload.results)) {
    return payload.results;
  }

  return [];
}
