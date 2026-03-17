import React from 'react';

import DataTablePage from './DataTablePage';

function Users() {
  return (
    <DataTablePage
      resource="users"
      title="Users"
      columns={[
        { key: 'id', label: 'ID' },
        { key: 'username', label: 'Username' },
        { key: 'email', label: 'Email' },
        { key: 'fitness_level', label: 'Fitness Level' },
        { key: 'team', label: 'Team' },
      ]}
    />
  );
}

export default Users;
