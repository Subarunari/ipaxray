# ipaxray
ipaxray extract Info.plist and embedded.mobileprovision from IPA file. Each parameter type is Dictionary.

# Requirements
more than python version 3.4.2.

# Usage

```python
from ipaxray import IpaFile

ipa_file = IpaFile(ipa_file_path)

# info.plist parameter
ipa_file.info_plist

# embedded.mobileprovision parameter
ipa_file.embedded_mobile_provision
```


# Error Type

| Error | Description |
|-------|:------------|
| NotFoundInfoPlistError | If ipa file does not contain Info.plist,this error occur. |
| NotFoundMobileProvisionError | If ipa file does not contain embedded.mobileprovision, this error occur. |
| InvalidApplicationError | If ipa file does not contain _CodeSignature/CodeResources, this error occur. |
