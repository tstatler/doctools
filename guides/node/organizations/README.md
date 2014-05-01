# Node.ACS & Platform Organizations #

<p class="note">This feature requires an Appcelerator Platform subscription.</p>

Starting with Node.ACS release 1.1.1, Node.ACS supports [Platform organizations](/platform/latest/#!/guide/Managing_Organizations). 
Note the following:

* Each Node.ACS application is assigned to exactly one organization
* All members of an organization, administrators and normal users, share applications that belong to that organization. Any member can make changes to any Node.ACS applications in that organization.
* Applications names must be unique within an organization.

When you [create](#!/guide/node_cli_new) a new Node.ACS application, you specify the ID of an organization to assign the application. Existing applications &mdash; those created before organization 
support was introduced &mdash; must be migrated to an organization. For information about this process see [About migration of existing Node.ACS applications](#node_orgs-section-about-migration-of-existing-node-acs-applications).

## About migration of existing Node.ACS applications ##

Applications that were created before organization support was added to Node.ACS do not, of course, belong to an organization. To migrate those applications to the new architecture, a "fake" organization for each user is created, and their applications are all assigned to that organization. This process is handled completely by Appcelerator.

By default, migrated applications are only visible to the user that created them. To assign an application to a specific organization so that it can be shared, please contact [Appcelerator Support](http://support2.appcelerator.com). Note that since application name must be unique if there is already an application in an organization with the same name as the application being migrated, it cannot be assigned to that organization.