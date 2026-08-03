# set comprehension
recipes={
    "Masala chai":["ginger","cardamom","clove"],
    "Elichai chai":["cardamom","milk"],
    "Spicy chai":["ginger","black pepper","clove"]
}
# this is a key value pair so it gives reference to make it iterable recipes.values()

unique_spices={spice for ingredients in recipes.values() for spice in ingredients }
# ingredients is [ginger,cardamom,clove] ingredients here is temporary(middle) so in place of expression the final value will come that is spice