db.createUser(
    {
        user: 'necati',
        pwd: 'necati',
        roles: [
            { role: "clusterMonitor", db: "admin" },
            { role: "dbOwner", db: "necati" },
            { role: 'readWrite', db: 'necati' }
        ]
    }
)
