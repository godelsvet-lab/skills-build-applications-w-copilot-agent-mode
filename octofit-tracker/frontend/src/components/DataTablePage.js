import React, { useEffect, useState } from 'react';

import { endpointFor, normalizeApiListPayload } from '../config';

function DataTablePage({ resource, title, columns }) {
  const [rows, setRows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const endpoint = endpointFor(resource);
    console.log(`[${resource}] endpoint`, endpoint);

    async function loadData() {
      try {
        const response = await fetch(endpoint);
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }
        const payload = await response.json();
        console.log(`[${resource}] payload`, payload);
        setRows(normalizeApiListPayload(payload));
      } catch (err) {
        setError(err.message || 'Unable to load data');
      } finally {
        setLoading(false);
      }
    }

    loadData();
  }, [resource]);

  return (
    <section className="card shadow-sm border-0">
      <div className="card-body">
        <h2 className="h4 mb-3">{title}</h2>
        {loading && <p className="text-secondary">Loading...</p>}
        {error && <div className="alert alert-danger py-2">{error}</div>}
        {!loading && !error && (
          <div className="table-responsive">
            <table className="table table-striped table-hover align-middle">
              <thead className="table-dark">
                <tr>
                  {columns.map((column) => (
                    <th key={column.key}>{column.label}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {rows.length === 0 && (
                  <tr>
                    <td colSpan={columns.length} className="text-center text-secondary">
                      No records found.
                    </td>
                  </tr>
                )}
                {rows.map((row, index) => (
                  <tr key={row.id || `${resource}-${index}`}>
                    {columns.map((column) => (
                      <td key={`${row.id || index}-${column.key}`}>
                        {String(row[column.key] ?? '-')}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </section>
  );
}

export default DataTablePage;
