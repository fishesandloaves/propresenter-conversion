import xml.etree.ElementTree as xmltree


class RVObject:

    def deserializexml(self, xmlelement):
        raise NotImplementedError("deserializexml() must be overridden in derived classes!")

    def serializexml(self):
        raise NotImplementedError("serializexml() must be overridden in derived classes!")

    def __repr__(self):
        reprstr = ""
        # Convert to effectively a JSON string.
        for curvar in vars(self).keys():
            reprstr = reprstr + "   @" + curvar + ": " + repr(getattr(self, curvar))

        return reprstr

    @staticmethod
    def createarray(rvXMLIvarName=""):
        arrayelement = xmltree.Element('array')
        arrayelement.set('rvXMLIvarName', rvXMLIvarName)
        return arrayelement

    @staticmethod
    def createdictionary(rvXMLIvarName=""):
        arrayelement = xmltree.Element('dictionary')
        arrayelement.set('rvXMLIvarName', rvXMLIvarName)
        return arrayelement

    @staticmethod
    def copyobject(obj):
        # Create a new object of that type.
        newobj = type(obj)(obj.serializexml())

        return newobj
