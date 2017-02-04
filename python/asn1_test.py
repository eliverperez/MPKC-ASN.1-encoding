from MPKC.MatsumotoImai.mi_record import MIPublicRecord

record = MIPublicRecord()
record.setComponentByName('primeField', 2)
record.setComponentByName('baseField', 2)
record.setComponentByName('extensionField', 2)
record.setComponentByName('nvars', 2)
record.setComponentByName('publicSystem', 2)
print(record.prettyPrint())
print('*********primeField: ' + str(record.getTagMap().keys()))

'''from pyasn1.type import univ, namedtype, tag
class Record(univ.Sequence):
  componentType = namedtype.NamedTypes(
    namedtype.NamedType('id', univ.Integer()),
    namedtype.OptionalNamedType(
      'room',
      univ.Integer().subtype(
        implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)
      )
    ),
    namedtype.DefaultedNamedType(
      'house', 
      univ.Integer(0).subtype(
        implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)
      )
    )
  )

record = Record()
print(record.prettyPrint())
record.setComponentByPosition(1, 321)
print(record.prettyPrint())
record.setDefaultComponents()
print(record.prettyPrint())'''
