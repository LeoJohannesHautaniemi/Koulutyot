kuukausi=int(input("Anna kuukauden numero"))
vuosi={12:"Talvi",1:"Talvi",2:"Talvi",3:"Kevät", 4:"Kevät",5:"Kevät",6:"Kesä", 7:"Kesä",8:"Kesä", 9:"Syksy",10:"Syksy",11:"Syksy"}
if kuukausi in vuosi:
    print(f"Se on {vuosi[kuukausi]}kuukausi")