import React from 'react';

import DataTablePage from './DataTablePage';

function Teams() {
  return (
    <DataTablePage
      resource="teams"
      title="Teams"
      columns={[
        { key: 'id', label: 'ID' },
        { key: 'name', label: 'Name' },
        { key: 'description', label: 'Description' },
      ]}
    />
  );
}

export default Teams;
