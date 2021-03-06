PGDMP     )        	            x         
   372_market     12.3 (Ubuntu 12.3-1.pgdg20.04+1)     12.3 (Ubuntu 12.3-1.pgdg20.04+1)     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16441 
   372_market    DATABASE     ~   CREATE DATABASE "372_market" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE "372_market";
                postgres    false            �            1259    16458    ENVANTER    TABLE     u   CREATE TABLE public."ENVANTER" (
    "Dukkan_id" text,
    "Urun_id" text,
    miktar numeric,
    public boolean
);
    DROP TABLE public."ENVANTER";
       public         heap    postgres    false            �            1259    16442 	   KULLANICI    TABLE     k   CREATE TABLE public."KULLANICI" (
    id text NOT NULL,
    isim text,
    soyisim text,
    image text
);
    DROP TABLE public."KULLANICI";
       public         heap    postgres    false            �            1259    16450    URUN    TABLE     �   CREATE TABLE public."URUN" (
    id text NOT NULL,
    isim text,
    detay text,
    firma text,
    fiyat money,
    image text
);
    DROP TABLE public."URUN";
       public         heap    postgres    false            �            1259    16488    User_payment_info    TABLE     ^   CREATE TABLE public."User_payment_info" (
    id numeric NOT NULL,
    card_number numeric
);
 '   DROP TABLE public."User_payment_info";
       public         heap    postgres    false            �            1259    16476    kullanıcı_adres    TABLE     W   CREATE TABLE public."kullanıcı_adres" (
    id numeric NOT NULL,
    address text
);
 '   DROP TABLE public."kullanıcı_adres";
       public         heap    postgres    false            �            1259    16482    kullanıcı_email    TABLE     U   CREATE TABLE public."kullanıcı_email" (
    id numeric NOT NULL,
    email text
);
 '   DROP TABLE public."kullanıcı_email";
       public         heap    postgres    false            �            1259    16470    kullanıcı_telefon    TABLE     W   CREATE TABLE public."kullanıcı_telefon" (
    id numeric NOT NULL,
    phone text
);
 )   DROP TABLE public."kullanıcı_telefon";
       public         heap    postgres    false            �            1259    16464    login    TABLE     p   CREATE TABLE public.login (
    id numeric NOT NULL,
    username text,
    password text,
    admin boolean
);
    DROP TABLE public.login;
       public         heap    postgres    false            �            1259    16494    shop    TABLE     n   CREATE TABLE public.shop (
    id numeric NOT NULL,
    name text,
    "check" boolean,
    rating numeric
);
    DROP TABLE public.shop;
       public         heap    postgres    false            �          0    16458    ENVANTER 
   TABLE DATA           L   COPY public."ENVANTER" ("Dukkan_id", "Urun_id", miktar, public) FROM stdin;
    public          postgres    false    204   �       �          0    16442 	   KULLANICI 
   TABLE DATA           ?   COPY public."KULLANICI" (id, isim, soyisim, image) FROM stdin;
    public          postgres    false    202          �          0    16450    URUN 
   TABLE DATA           F   COPY public."URUN" (id, isim, detay, firma, fiyat, image) FROM stdin;
    public          postgres    false    203   {       �          0    16488    User_payment_info 
   TABLE DATA           >   COPY public."User_payment_info" (id, card_number) FROM stdin;
    public          postgres    false    209   �       �          0    16476    kullanıcı_adres 
   TABLE DATA           :   COPY public."kullanıcı_adres" (id, address) FROM stdin;
    public          postgres    false    207   
       �          0    16482    kullanıcı_email 
   TABLE DATA           8   COPY public."kullanıcı_email" (id, email) FROM stdin;
    public          postgres    false    208   H       �          0    16470    kullanıcı_telefon 
   TABLE DATA           :   COPY public."kullanıcı_telefon" (id, phone) FROM stdin;
    public          postgres    false    206   �       �          0    16464    login 
   TABLE DATA           >   COPY public.login (id, username, password, admin) FROM stdin;
    public          postgres    false    205   �       �          0    16494    shop 
   TABLE DATA           9   COPY public.shop (id, name, "check", rating) FROM stdin;
    public          postgres    false    210          8           2606    16449    KULLANICI KULLANICI_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public."KULLANICI"
    ADD CONSTRAINT "KULLANICI_pkey" PRIMARY KEY (id);
 F   ALTER TABLE ONLY public."KULLANICI" DROP CONSTRAINT "KULLANICI_pkey";
       public            postgres    false    202            :           2606    16457    URUN URUN_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public."URUN"
    ADD CONSTRAINT "URUN_pkey" PRIMARY KEY (id);
 <   ALTER TABLE ONLY public."URUN" DROP CONSTRAINT "URUN_pkey";
       public            postgres    false    203            �   G   x�32742221��4��L89Ӹ���p� ���[���c7@5������h�)�z�8H}� v�      �   \   x�3��O/�R�NL�S�*ί䄐%%�V���e�%�E�z�%�I�ũE��y%�y%z��������F���&�Ŷ&fje�&\1z\\\ ok�      �   b  x�m�Kn�0�s
 ǯ�$�A	ъ��*!���b��=V�ӓ4 �c5ү�ѧƃ���`2X�?6oS��m-�Z*�=��8�������t�?� ��h�0�e�Ld�r��V�j_}�+�ݧ>!yj��Q*�Q �բD�Y6H�:ֹF���:{җsU��{8&(c���'����@+ka\�
j��KJ:�a�^��9hk�]F�Or��Dq�;<敐�}���|^��eo=c�6���x����uS�nz>g�v�a{��(LS&pZYA�B8��C����"Mq-W�0FY��u%���BI-�.D�f���"�s���~�"DSL�U��X���8�蓒�      �      x������ � �      �   .   x�3�t�ILJ�MTp�,���K�H�U�2�T��/�H-J����� �$      �   4   x�3��O/��NL��˯*ίt��/�M���K��U�2�T@�N�Ir��qqq ��e      �   #   x�3�405655�450�T�2�T0 �L�b���� K�      �   3   x�3�L�IK�/�LO���442�,�2�LJ-I�O.�/�462�L����� ��      �      x������ � �     