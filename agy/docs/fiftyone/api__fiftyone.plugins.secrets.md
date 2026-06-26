---
source_url: https://docs.voxel51.com/api/fiftyone.plugins.secrets.html
---

# fiftyone.plugins.secrets#

Plugin secrets resolver.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`PluginSecretsResolver`() | Injects secrets from environmental variables into the execution context.  
---|---  
`SecretsDictionary`(secrets_dict[,Â ...]) | A more secure dictionary for accessing plugin secrets in operators that will attempt to resolve missing plugin secrets upon access.  
  
class fiftyone.plugins.secrets.PluginSecretsResolver#
    

Bases: `object`

Injects secrets from environmental variables into the execution context.

**Methods:**

`register_operator`(operator_uri,Â required_secrets) |   
---|---  
`client`() |   
`get_multiple`(keys,Â operator_uri,Â **kwargs) | Get the value of multiple secrets.  
`get_secret`(key,Â operator_uri,Â **kwargs) | Get the value of a secret.  
`get_secret_sync`(key,Â operator_uri,Â **kwargs) | Get the value of a secret.  
  
register_operator(_operator_uri : str_, _required_secrets : List[str]_) → None#
    

client() → ISecretProvider#
    

async get_multiple(_keys : List[str]_, _operator_uri : str_, _** kwargs_) → Dict[str, ISecret | None]#
    

Get the value of multiple secrets. :param keys: list of secret keys :param operator_uri: the operator URI :param kwargs: additional keyword arguments to pass to the secrets :param client for authentication if required:

Returns:
    

A dictionary of secret keys and their values

async get_secret(_key : str_, _operator_uri : str_, _** kwargs_) → ISecret | None#
    

Get the value of a secret.

Parameters:
    

  * **key** (_str_) â unique secret identifier

  * **kwargs** â additional keyword arguments to pass to the secrets

  * **required** (_client for authentication if_)




get_secret_sync(_key : str_, _operator_uri : str_, _** kwargs_) → ISecret | None#
    

Get the value of a secret.

Parameters:
    

  * **key** (_str_) â unique secret identifier

  * **kwargs** â additional keyword arguments to pass to the secrets

  * **required** (_client for authentication if_)




class fiftyone.plugins.secrets.SecretsDictionary(_secrets_dict : Dict[str, str]_, _operator_uri : str = None_, _resolver_fn : Callable = None_, _required_keys : List[str] = None_)#
    

Bases: `object`

A more secure dictionary for accessing plugin secrets in operators that will attempt to resolve missing plugin secrets upon access.

**Methods:**

`copy`() |   
---|---  
`keys`() |   
`values`() |   
`items`() |   
`get`(key[,Â default]) |   
  
copy()#
    

keys()#
    

values()#
    

items()#
    

get(_key_ , _default =None_)#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
