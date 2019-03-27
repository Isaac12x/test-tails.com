from flask import request, redirect, render_template, url_for, flash
from main.app import app
from main.app.api_utils import PostcodeFinder
from main.app.forms import NewStoreForm
from main.app.utils import load_data, write_to_file, get_and_insert, order_list


@app.errorhandler(404)
def render_page_not_found(error):
    return render_template("404.html"), 404


@app.route("/")
def render_index():
    filepath = "main/app/stores.json"
    # load stores and pass them
    stores = load_data(filepath)

    try:
        if stores[0]["lat"]:
            pass
    except KeyError:
        length_of_stores = len(stores) - 1
        stores_with_coordinates = [
            get_and_insert(store)
            for index, store in enumerate(stores)
            if store is not None and index < length_of_stores
        ]
        stores_with_coordinates = order_list(stores_with_coordinates)
        write_to_file(stores_with_coordinates, filepath)

    return render_template("index.html", title="Tails.com - All stores", stores=stores)


@app.route("/add-store", methods=["GET", "POST"])
def add_store():
    form = NewStoreForm()
    if form.validate_on_submit():
        flash("Adding new store")

        # this will be better suited for a custom validator
        valid = PostcodeFinder.validate_postcode(form.postcode.data)
        if valid:
            lat, long = PostcodeFinder.get_postcode_coords(
                form.postcode.data, validate=False
            )

            stores = load_data("main/app/stores.json")
            stores.append(
                {
                    "name": form.name.data,
                    "postcode": form.postcode.data,
                    "lat": lat,
                    "long": long,
                }
            )

            write_to_file(stores, "main/app/stores.json")

            flash("Added new store")
            return redirect("/")

        flash("The postcode does not exist")
    return render_template(
        "new_store_form.html", title="Tails.com - Add store", form=form
    )
