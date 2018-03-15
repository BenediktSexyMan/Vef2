# API
# 1
Vefþjónusta er forrit sem að notar http til þess að senda gögn á milli tölva í máli eins og JSON eða XML meðan API virkar meira eins og milliliður til þess að senda kóða sem mun svo vora execute-aður þar sem að requestið kom frá.
# 2
### JSON
```JSON

{
  "orders": [
    {
      "crust": "original",
      "toppings": [
        "cheese",
        "pepperoni",
        "garlic"
      ],
      "status": "cooking",
      "customer": {
        "name": "John Doe",
        "phone": "+3541234567"
      }
    }
  ]
}
```
### XML
```XML
<?xml version="1.0" encoding="UTF-8"?>
<root>
   <orders>
      <element>
         <crust>original</crust>
         <customer>
            <name>John Doe</name>
            <phone>+3541234567</phone>
         </customer>
         <status>cooking</status>
         <toppings>
            <element>cheese</element>
            <element>pepperoni</element>
            <element>garlic</element>
         </toppings>
      </element>
   </orders>
</root>
```
# 3
OSI model-ið er skilgreining af skiptingu data virkni tölvunar þar sem að hvert layer tekur við ákveðnum upplýsingum, vinnur með þær og sendir þær svo í næsta layer fyrir ofan sig.
# 4
RESTful API er api sem að notar http command-in (get, post etc) til þess að vinna með gögn. Til þess að vera restful þá þarf virknin að vera stateless og að client-inn þarf aldrei að spá í hvernig að það sé tekið á móti gögnunum sínum.
# 5
## HTTP Request
Á ég virkilega að trúa því að það sé verið að biðja mig um að útskýra þetta í fjórðu önn af vefhönnunar námi?
## HTTP Response
Á ég virkilega að trúa því að það sé verið að biðja mig um að útskýra þetta í fjórðu önn af vefhönnunar námi?
# 6
OAuth er aðferð til þess að leyfa forriti að fá lykil(frá síðum eins og facebook) sem gefur manni aðgang að opinberum notanda upplýsingum.
# 7.2
This is not question #7. This is question #7.2., and question #7 was not here.
