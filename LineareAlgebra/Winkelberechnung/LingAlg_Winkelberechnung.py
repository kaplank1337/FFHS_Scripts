import numpy as np

def berechne_norm(vektor):
    """
    Berechnet die Norm eines Vektors.
    """
    return np.linalg.norm(vektor)

def winkel_geraden(v1, v2):
    """
    Berechnet den Winkel zwischen zwei Geraden.
    """
    print("\n=== Winkel zwischen zwei Geraden ===")
    print(f"Richtungsvektor der ersten Geraden: {v1}")
    print(f"Richtungsvektor der zweiten Geraden: {v2}")

    # Schritt 1: Skalarprodukt berechnen
    skalarprodukt = np.dot(v1, v2)
    print(f"Schritt 1: Skalarprodukt: {skalarprodukt}")

    # Schritt 2: Länge der Vektoren berechnen
    länge_v1 = berechne_norm(v1)
    länge_v2 = berechne_norm(v2)
    print(f"Schritt 2: Länge von v1: {länge_v1}, Länge von v2: {länge_v2}")

    # Schritt 3: Cosinus des Winkels berechnen
    cos_phi = skalarprodukt / (länge_v1 * länge_v2)
    print(f"Schritt 3: cos(φ) = {cos_phi}")

    # Schritt 4: Winkel berechnen
    phi = np.arccos(np.clip(cos_phi, -1.0, 1.0))  # Clip für numerische Stabilität
    phi_grad = np.degrees(phi)
    print(f"Schritt 4: Winkel φ = {phi} (in Radiant)")
    print(f"Winkel in Grad: {phi_grad}°")
    return phi, phi_grad


def winkel_gerade_ebene(gerade, ebene_normal):
    """
    Berechnet den Winkel zwischen einer Geraden und einer Ebene.
    """
    print("\n=== Winkel zwischen einer Geraden und einer Ebene ===")
    print(f"Richtungsvektor der Geraden: {gerade}")
    print(f"Normalenvektor der Ebene: {ebene_normal}")

    # Schritt 1: Skalarprodukt berechnen
    skalarprodukt = np.dot(gerade, ebene_normal)
    print(f"Schritt 1: Skalarprodukt: {skalarprodukt}")

    # Schritt 2: Länge der Vektoren berechnen
    länge_gerade = berechne_norm(gerade)
    länge_ebene_normal = berechne_norm(ebene_normal)
    print(f"Schritt 2: Länge der Vektoren: Gerade: {länge_gerade}, Ebene: {länge_ebene_normal}")

    # Schritt 3: Sinus des Winkels berechnen
    sin_phi = np.abs(skalarprodukt) / (länge_gerade * länge_ebene_normal)
    print(f"Schritt 3: sin(φ) = {sin_phi}")

    # Schritt 4: Komplementärwinkel berechnen
    phi = np.arcsin(np.clip(sin_phi, -1.0, 1.0))
    theta = np.pi / 2 - phi
    theta_grad = np.degrees(theta)
    print(f"Schritt 4: Komplementärwinkel θ = {theta} (in Radiant)")
    print(f"Winkel in Grad: {theta_grad}°")
    return theta, theta_grad


def winkel_ebenen(n1, n2):
    """
    Berechnet den Winkel zwischen zwei Ebenen.
    """
    print("\n=== Winkel zwischen zwei Ebenen ===")
    print(f"Normalenvektor der ersten Ebene: {n1}")
    print(f"Normalenvektor der zweiten Ebene: {n2}")

    # Schritt 1: Skalarprodukt berechnen
    skalarprodukt = np.dot(n1, n2)
    print(f"Schritt 1: Skalarprodukt: {skalarprodukt}")

    # Schritt 2: Länge der Vektoren berechnen
    länge_n1 = berechne_norm(n1)
    länge_n2 = berechne_norm(n2)
    print(f"Schritt 2: Länge von n1: {länge_n1}, Länge von n2: {länge_n2}")

    # Schritt 3: Cosinus des Winkels berechnen
    cos_phi = np.abs(skalarprodukt) / (länge_n1 * länge_n2)
    print(f"Schritt 3: cos(φ) = {cos_phi}")

    # Schritt 4: Winkel berechnen
    phi = np.arccos(np.clip(cos_phi, -1.0, 1.0))
    phi_grad = np.degrees(phi)
    print(f"Schritt 4: Winkel φ = {phi} (in Radiant)")
    print(f"Winkel in Grad: {phi_grad}°")
    return phi, phi_grad


if __name__ == "__main__":
    # Beispiel: Winkel zwischen zwei Geraden
    v1 = np.array([2, 1, 0])
    v2 = np.array([1, 1, 1])
    winkel_geraden(v1, v2)

    # Beispiel: Winkel zwischen einer Geraden und einer Ebene
    gerade = np.array([2, -1, 1])
    ebene_normal = np.array([1, 2, -1])
    winkel_gerade_ebene(gerade, ebene_normal)

    # Beispiel: Winkel zwischen zwei Ebenen
    n1 = np.array([2, 3, -1])
    n2 = np.array([1, -2, 4])
    winkel_ebenen(n1, n2)
