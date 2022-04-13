/* const image_input = document.querySelector("#image_input");
const image_preview = document.querySelector("#image_preview");
let uploaded_image;
image_input.addEventListener("change", function() {
	const reader = new FileReader();
	image_input.addEventListener("load", () => {
		uploaded_image = reader.result;
		image_preview.style.backgroundImage = `url(${uploaded_image})`;
	});
	reader.readAsDataURL(this.files[0]);
}); */