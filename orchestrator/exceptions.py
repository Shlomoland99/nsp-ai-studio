class NSPError(Exception): pass
class ConfigurationError(NSPError): pass
class ProviderUnavailable(NSPError): pass
class RoutingError(NSPError): pass
class ConsentRequired(NSPError): pass
