filename=input("Enter your filename:")
part=filename.rsplit('.',1)
if len(part)>1:
    print("the extension is",part[-1])
else:
    print("no extension found")