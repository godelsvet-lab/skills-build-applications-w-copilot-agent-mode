import React from 'react';

import DataTablePage from './DataTablePage';

function Activities() {
  return (
    <DataTablePage
      resource="activities"
      title="Activities"
      columns={[
        { key: 'id', label: 'ID' },
        { key: 'user', label: 'User' },
        { key: 'activity_type', label: 'Activity Type' },
        { key: 'duration_minutes', label: 'Duration (min)' },
        { key: 'calories_burned', label: 'Calories' },
        { key: 'points', label: 'Points' },
        { key: 'date', label: 'Date' },
      ]}
    />
  );
}

export default Activities;
