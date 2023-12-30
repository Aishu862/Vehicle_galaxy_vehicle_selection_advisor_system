// handling drop down hover effect on nav links

const navLink = ["#link-1", "#link-2", "#link-3", "#link-4", "#link-5"];

for (let i = 1; i <= 5; i++) {
  const link = document.querySelector(navLink[i - 1]);
  link.addEventListener("mouseover", () => {
    const dropDown = document.querySelector(`#drop-down${i}`);
    dropDown.style.top = "55px";
    console.log("ppp");
  });

  link.addEventListener("mouseout", () => {
    const dropDown = document.querySelector(`#drop-down${i}`);
    dropDown.style.top = "-600px";
    console.log("ppp");
  });
}

//handling carousal slider on home page
const carousalBtn = [
  "#carousal-btn-1",
  "#carousal-btn-2",
  "#carousal-btn-3",
  "#carousal-btn-4",
];

for (let i = 1; i <= 4; i++) {
  const btn = document.querySelector(carousalBtn[i - 1]);
  btn.addEventListener("click", () => {
    for (let j = 1; j <= 4; j++) {
      const nonActiveSlider = document.querySelector(`#carousal-img-${j}`);
      nonActiveSlider.classList.remove("carousal-active");

      const nonActiveBtn = document.querySelector(`#carousal-btn-${j}`);
      nonActiveBtn.classList.remove("carousal-btn-active");
    }
    const activeSlider = document.querySelector(`#carousal-img-${i}`);
    activeSlider.classList.add("carousal-active");

    const activeBtn = document.querySelector(`#carousal-btn-${i}`);
    activeBtn.classList.add("carousal-btn-active");
  });
}
