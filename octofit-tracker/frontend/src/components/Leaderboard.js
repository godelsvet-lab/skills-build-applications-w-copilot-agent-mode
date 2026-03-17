import React from 'react';

import DataTablePage from './DataTablePage';

function Leaderboard() {
  return (
    <DataTablePage
      resource="leaderboard"
      title="Leaderboard"
      columns={[
        { key: 'rank', label: 'Rank' },
        { key: 'user', label: 'User' },
        { key: 'team', label: 'Team' },
        { key: 'total_points', label: 'Total Points' },
        { key: 'updated_at', label: 'Updated' },
      ]}
    />
  );
}

export default Leaderboard;
