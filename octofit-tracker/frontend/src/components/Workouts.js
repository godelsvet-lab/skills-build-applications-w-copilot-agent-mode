import React from 'react';

import DataTablePage from './DataTablePage';

function Workouts() {
  return (
    <DataTablePage
      resource="workouts"
      title="Workout Suggestions"
      columns={[
        { key: 'id', label: 'ID' },
        { key: 'user', label: 'User' },
        { key: 'title', label: 'Title' },
        { key: 'difficulty', label: 'Difficulty' },
        { key: 'description', label: 'Description' },
      ]}
    />
  );
}

export default Workouts;
