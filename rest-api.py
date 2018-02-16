"""
https://docs.oracle.com/en/cloud/iaas/compute-iaas-cloud/stcsa/rest-endpoints.html

todo: ACL:

Retrieve Details of an ACL
Method: GET
Path: /network/v1/acl/{name}

Retrieve Details of all ACLs in a Container
Method: GET
Path: /network/v1/acl/{container}/

todo: Accounts:

Retrieve Details of all Accounts in a Container
Method: GET
Path: /account/{container}/

Retrieve Details of an Account
Method: GET
Path: /account/{name}

Retrieve Names of all Accounts and Subcontainers in a Container
Method: GET
Path: /account/{container}

Retrieve Names of Containers
Method: GET
Path: /account/


todo: Backup Configurations:

Retrieve Details of a Backup Configuration
Method: GET
Path: /backupservice/v1/configuration/{name}

Retrieve Details of All Backup Configurations
Method: GET
Path: /backupservice/v1/configuration

todo: Backups

Retrieve Details of all Backups
Method: GET
Path: /backupservice/v1/backup

Retrieves Details of the Specified Backup
Method: GET
Path: /backupservice/v1/backup/{name}

todo: IPAddressAssociations

Retrieve Details of all IP Address Associations in a Container
Method: GET
Path: /network/v1/ipassociation/{container}/

Retrieve Details of an IP Address Association Used in IP Networks
Method: GET
Path: /network/v1/ipassociation/{name}

todo: IPAddressPrefixSets

Retrieve Details of all IP Address Prefix Sets in a Container
Method: GET
Path: /network/v1/ipaddressprefixset/{container}/

Retrieve Details of an IP Address Prefix Set
Method: GET
Path: /network/v1/ipaddressprefixset/{name}

todo: IPAddressReservations

Retrieve Details of all IP Address Reservations in a Container
Method: GET
Path: /network/v1/ipreservation/{container}/

Retrieve Details of an IP Address Reservation Used in IP Networks
Method: GET
Path: /network/v1/ipreservation/{name}

todo: IPAssociations

Retrieve Details of all IP Associations in a Container
Method: GET
Path: /ip/association/{container}/

Retrieve Details of an IP Association
Method: GET
Path: /ip/association/{name}

Retrieve Names of all IP Associations and Subcontainers in a Container
Method: GET
Path: /ip/association/{container}

Retrieve Names of Containers
Method: GET
Path: /ip/association/

todo: IPNetworkExchanges

Retrieve Details of all IP Network Exchanges in a Container
Method: GET
Path: /network/v1/ipnetworkexchange/{container}/

Retrieve Details of an IP Network Exchange
Method: GET
Path: /network/v1/ipnetworkexchange/{name}

todo: IPNetworks

Retrieve Details of all IP Networks in a Container
Method: GET
Path: /network/v1/ipnetwork/{container}/

Retrieve Details of an IP Network
Method: GET
Path: /network/v1/ipnetwork/{name}

todo: IPReservations

Retrieve Details of all IP Reservations in a Container
Method: GET
Path: /ip/reservation/{container}/

Retrieve Details of an IP Reservation
Method: GET
Path: /ip/reservation/{name}

Retrieve Names of all IP Reservations and Subcontainers in a Container
Method: GET
Path: /ip/reservation/{container}

Retrieve Names of Containers
Method: GET
Path: /ip/reservation/

todo: ImageListEntries

Retrieve Details of an Image List Entry
Method: GET
Path: /imagelist/{name}/entry/{version}

todo: ImageLists

Retrieve Details of all Image Lists in a Container
Method: GET
Path: /imagelist/{container}/

Retrieve Details of an Image List
Method: GET
Path: /imagelist/{name}

Retrieve Names of all Image Lists and Subcontainers in a Container
Method: GET
Path: /imagelist/{container}

Retrieve Names of Containers
Method: GET
Path: /imagelist/

todo: Instances

Retrieve Details of all Instances in a Container
Method: GET
Path: /instance/{container}/

Retrieve Details of an Instance
Method: GET
Path: /instance/{name}

Retrieve Names of all Instances and Subcontainers in a Container
Method: GET
Path: /instance/{container}

Retrieve Names of Containers
Method: GET
Path: /instance/

todo: MachineImages

Retrieve Details of a Machine Image
Method: GET
Path: /machineimage/{name}

Retrieve Details of all Machine Images in a Container
Method: GET
Path: /machineimage/{container}/

Retrieve Names of all Machine Images and Subcontainers in a Container
Method: GET
Path: /machineimage/{container}

Retrieve Names of Containers
Method: GET
Path: /machineimage/

todo: OSSContainers

Retrieve Details of all Oracle Cloud Infrastructure Object Storage Classic Containers in a Container
Method: GET
Path: /integrations/osscontainer/{container}/

Retrieve Details of an Oracle Cloud Infrastructure Object Storage Classic Container
Method: GET
Path: /integrations/osscontainer/{name}

Retrieve Names of all Oracle Cloud Infrastructure Object Storage Classic Containers and Subcontainers in a Container
Method: GET
Path: /integrations/osscontainer/{container}

Retrieve Names of Containers
Method: GET
Path: /integrations/osscontainer/

todo: PrivateGateways

Retrieve Details of a Private Gateway
Method: GET
Path: /network/v1/privategateway/{name}

Retrieve Details of all Private Gateways in a Container
Method: GET
Path: /network/v1/privategateway/{container}/

Retrieve Names of all Private Gateways and Subcontainers in a Container
Method: GET
Path: /network/v1/privategateway/{container}

todo: RebootInstanceRequests

Retrieve Details of a Reboot Instance Request
Method: GET
Path: /rebootinstancerequest/{name}

Retrieve Details of all Reboot Instance Requests in a Container
Method: GET
Path: /rebootinstancerequest/{container}/

Retrieve Names of all Reboot Instance Requests and Subcontainers in a Container
Method: GET
Path: /rebootinstancerequest/{container}

Retrieve Names of Containers
Method: GET
Path: /rebootinstancerequest/

# Refresh an Authentication Token
# Method: GET
# Path: /refresh/

todo: Routes

Retrieve Details of a Route
Method: GET
Path: /network/v1/route/{name}

Retrieve Details of all Routes in a Container
Method: GET
Path: /network/v1/route/{container}/

todo: SecApplications

Retrieve Details of a Security Application
Method: GET
Path: /secapplication/{name}

Retrieve Details of all Security Applications in a Container
Method: GET
Path: /secapplication/{container}/

Retrieve Names of all Security Applications and Subcontainers in a Container
Method: GET
Path: /secapplication/{container}

Retrieve Names of Containers
Method: GET
Path: /secapplication/

todo: SecAssociations

Retrieve Details of a Security Association
Method: GET
Path: /secassociation/{name}

Retrieve Details of all Security Associations in a Container
Method: GET
Path: /secassociation/{container}/

Retrieve Names of all Security Associations and Subcontainers in a Container
Method: GET
Path: /secassociation/{container}

Retrieve Names of Containers
Method: GET
Path: /secassociation/

todo: SecIPLists

Retrieve Details of a Security IP List
Method: GET
Path: /seciplist/{name}

Retrieve Details of all Security IP Lists in a Container
Method: GET
Path: /seciplist/{container}/

Retrieve Names of all Security IP Lists and Subcontainers in a Container
Method: GET
Path: /seciplist/{container}

Retrieve Names of Containers
Method: GET
Path: /seciplist/

todo: SecLists

Retrieve Details of a Security List
Method: GET
Path: /seclist/{name}

Retrieve Details of all Security Lists in a Container
Method: GET
Path: /seclist/{container}/

Retrieve Names of all Security Lists and Subcontainers in a Container
Method: GET
Path: /seclist/{container}

Retrieve Names of Containers
Method: GET
Path: /seclist/

todo: SecRules

Retrieve Details of a Security Rule
Method: GET
Path: /secrule/{name}

Retrieve Details of all Security Rules in a Container
Method: GET
Path: /secrule/{container}/

Retrieve Names of all Security Rules and Subcontainers in a Container
Method: GET
Path: /secrule/{container}

Retrieve Names of Containers
Method: GET
Path: /secrule/

todo: SecurityProtocols

Retrieve Details of a Security Protocol Used in IP Networks
Method: GET
Path: /network/v1/secprotocol/{name}

Retrieve Details of all Security Protocols in a Container
Method: GET
Path: /network/v1/secprotocol/{container}/

todo: SecurityRules

Retrieve Details of a Security Rule Used in IP Networks
Method: GET
Path: /network/v1/secrule/{name}

Retrieve Details of all Security Rules in a Container
Method: GET
Path: /network/v1/secrule/{container}/

todo: Shapes

Retrieve Details of a Shape
Method: GET
Path: /shape/{name}

Retrieve Details of all Shapes
Method: GET
Path: /shape/

todo: StorageAttachments

Retrieve Details of a Storage Attachment
Method: GET
Path: /storage/attachment/{name}

Retrieve Details of all Storage Attachments in a Container
Method: GET
Path: /storage/attachment/{container}/

Retrieve Names of all Storage Attachments and Subcontainers in a Container
Method: GET
Path: /storage/attachment/{container}

Retrieve Names of Containers
Method: GET
Path: /storage/attachment/

todo: StorageProperties

Retrieve Details of a Storage Property
Method: GET
Path: /property/storage/{name}

Retrieve Details of all Storage Properties in a Container
Method: GET
Path: /property/storage/{container}/

Retrieve Names of all Storage Properties and Subcontainers in a Container
Method: GET
Path: /property/storage/{container}

Retrieve Names of Containers
Method: GET
Path: /property/storage/

todo: StorageVolumes

Retrieve Details of a Storage Volume
Method: GET
Path: /storage/volume/{name}

Retrieve Details of all Storage Volumes in a Container
Method: GET
Path: /storage/volume/{container}/

Retrieve Names of all Storage Volumes and Subcontainers in a Container
Method: GET
Path: /storage/volume/{container}

Retrieve Names of Containers
Method: GET
Path: /storage/volume/

todo: VPNEndpointV2s

Retrieve Details of a VPN Endpoint V2
Method: GET
Path: /vpnendpoint/v2/{name}

Retrieve Details of all VPN Endpoint V2s in a Container
Method: GET
Path: /vpnendpoint/v2/{container}/

todo: VPNEndpoints

Retrieve Details of a VPN Endpoint
Method: GET
Path: /vpnendpoint/{name}

Retrieve Details of all VPN Endpoints in a Container
Method: GET
Path: /vpnendpoint/{container}/

todo: VirtualNICSets

Retrieve Details of a Virtual NIC Set
Method: GET
Path: /network/v1/vnicset/{name}

Retrieve Details of all Virtual NIC Sets in a Container
Method: GET
Path: /network/v1/vnicset/{container}/

todo: VirtualNICs

Retrieve Details of a Virtual NIC
Method: GET
Path: /network/v1/vnic/{name}

Retrieve Details of all Virtual NICs in a Container
Method: GET
Path: /network/v1/vnic/{container}/

"""