import ecdsa
import hashlib
import binascii
def create_wallet() -> dict:
    human_data = dict()

    ecdsa_private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    human_data['private_key'] = ecdsa_private_key.to_string().hex() 
    
    ecdsa_public_key = ecdsa_private_key.get_verifying_key().to_string().hex() # type: ignore
    human_data['public_key'] = ecdsa_public_key

    return human_data


create_wallet()