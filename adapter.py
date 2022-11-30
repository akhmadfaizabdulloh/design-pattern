class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self) -> str:
        return ".lanoisgnuf namargormep salek id gnatad tamaleS"


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Klien: Saya dapat bekerja dengan baik dengan objek Target:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Klien: Class Adaptee memiliki antarmuka yang aneh. "
          "Lihat, saya tidak mengerti:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Klien: Tapi saya bisa mengerjakannya melalui Adaptor:")
    adapter = Adapter()
    client_code(adapter)
    print("\n")
