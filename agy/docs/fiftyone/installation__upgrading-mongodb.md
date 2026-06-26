---
source_url: https://docs.voxel51.com/installation/upgrading-mongodb.html
---

# Upgrading MongoDB#

The instructions on this page apply to FiftyOne users who are using the MongoDB binary that is bundled with FiftyOne.

If you utilize a [custom/shared MongoDB database](user_guide__config.md#configuring-mongodb-connection), then follow the upgrade path advised by your database provider.

Note

It is strongly recommended to perform a backup of your MongoDB database before upgrading your MongoDB version.

## Upgrading to MongoDB 8#

  1. Close any Python sessions that are running `fiftyone`

  2. Ensure that the bundled mongo process has been shut down



    
    
    ps -ef | egrep "fiftyone.*mongod"
    
    
    
    ps -ef | egrep "fiftyone.*mongod"
    
    
    
    Get-Process | \
        Where-Object { \
            $_.Name -like "*fiftyone*" \
            -and $_.Name -like "*mongod*" \
        }
    

  3. Upgrade to `fiftyone>=1.3` and `fiftyone-db>=1.2.0`
         
         pip install --upgrade fiftyone fiftyone[db]
         

  4. [Install mongosh](https://www.mongodb.com/docs/mongodb-shell/install)

  5. Find the MongoDB URI using your operating systemâs network libraries



    
    
    sudo lsof -iTCP -sTCP:LISTEN -P -n | egrep "mongod"
    
    
    
    sudo lsof -iTCP -sTCP:LISTEN -P -n | egrep "mongod"
    
    
    
    Get-NetTCPConnection | \
        Where-Object { $_.State -eq 'Listen' } | \
        Select-String -Pattern "mongod"
    

  6. Connect to MongoDB using `mongosh`
         
         mongosh "$URI_FROM_ABOVE"
         

  7. Enable [backwards-incompatible MongoDB 8.0 features](https://www.mongodb.com/docs/manual/release-notes/8.0-upgrade-standalone/#enable-backwards-incompatible--features) by setting your databaseâs feature compatibility version
         
         db.adminCommand({
             setFeatureCompatibilityVersion: "8.0",
             confirm: true
         })
         
         // Verify the upgrade
         db.adminCommand({
             getParameter: 1,
             featureCompatibilityVersion: 1
         })
         




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
