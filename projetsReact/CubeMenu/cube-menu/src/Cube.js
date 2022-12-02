import React, { useState, useEffect, useMemo } from "react";
import "./Cube.scss";

export default function Cube() {
  const [isZoomOut, setZoomOut] = useState(false);
  const [onMotion, setOnMotion] = useState(false);
  const [rotation, setRotation] = useState({
    originX: 0,
    originY: 0,
    originZ: 0,
    X: 0,
    Y: 0,
    Z: 0,
  });
  const [mouseOrigin, setMouseOrigin] = useState({
    mouseX: 0,
    mouseY: 0,
  });

  function handleWheel(event) {
    if (event.deltaY > 0) {
      setZoomOut(true);
      document.body.classList.add("zoomOut");
      const size = getComputedStyle(document.documentElement).getPropertyValue(
        `--size`
      );
    } else {
      setZoomOut(false);
      document.body.classList.remove("zoomOut");
    }
  }

  const handleMouseDown = (event) => {
    setOnMotion(true);
    setMouseOrigin({
      mouseX: event.clientX,
      mouseY: event.clientY,
    });
  };

  const handleMouseUp = () => {
    setOnMotion(false);
    setMouseOrigin({ mouseX: 0, mouseY: 0 });
    var newOriginX =
      rotation.X >= 0
        ? Math.trunc((rotation.X + 45) / 90) * 90
        : Math.trunc((rotation.X - 45) / 90) * 90;
    var newOriginY =
      rotation.Y >= 0
        ? Math.trunc((rotation.Y + 45) / 90) * 90
        : Math.trunc((rotation.Y - 45) / 90) * 90;
    var newOriginZ =
      rotation.Z >= 0
        ? Math.trunc((rotation.Z + 45) / 90) * 90
        : Math.trunc((rotation.Z - 45) / 90) * 90;
    setRotation({
      originX: newOriginX,
      originY: newOriginY,
      originZ: newOriginZ,
      X: newOriginX,
      Y: newOriginY,
      Z: newOriginZ,
    });
  };
  console.log("X:", Math.trunc(rotation.X / 90) % 4);
  const handleMouseMove = (event) => {
    if (onMotion && isZoomOut) {
      var deltaX = mouseOrigin.mouseX - event.clientX;
      var deltaY = mouseOrigin.mouseY - event.clientY;
      if (Math.trunc(rotation.originX / 90) % 4 === 0) {
        setRotation((prev) => ({
          ...prev,
          X: rotation.originX + deltaY / 3,
          Y: rotation.originY - deltaX / 3,
        }));
      } else if (
        Math.trunc(rotation.originX / 90) % 4 === 1 ||
        Math.trunc(rotation.originX / 90) % 4 === -3
      ) {
        setRotation((prev) => ({
          ...prev,
          X: rotation.originX + deltaY / 3,
          Z: rotation.originZ + deltaX / 3,
        }));
      } else if (
        Math.trunc(rotation.originX / 90) % 4 === 2 ||
        Math.trunc(rotation.originX / 90) % 4 === -2
      ) {
        setRotation((prev) => ({
          ...prev,
          X: rotation.originX + deltaY / 3,
          Y: rotation.originY + deltaX / 3,
        }));
      } else if (
        Math.trunc(rotation.originX / 90) % 4 === -1 ||
        Math.trunc(rotation.originX / 90) % 4 === 3
      ) {
        setRotation((prev) => ({
          ...prev,
          X: rotation.originX + deltaY / 3,
          Z: rotation.originZ - deltaX / 3,
        }));
      }
    }
  };

  useEffect(() => {
    var scene = document.getElementById("scene");
    if (onMotion) {
      scene.style.transition = "all 0s";
    } else {
      scene.style.transition = "all 0.5s";
    }

    scene.style.transform = `rotateX(${rotation.X}deg) rotateY(${rotation.Y}deg) rotateZ(${rotation.Z}deg)`;
  }, [onMotion, rotation.X, rotation.Y, rotation.Z]);

  return (
    <div
      className="layout"
      onMouseDown={(e) => handleMouseDown(e)}
      onMouseMove={(e) => handleMouseMove(e)}
      onMouseUp={(e) => handleMouseUp(e)}
      onWheel={(e) => handleWheel(e)}>
      <div id="scene">
        <div className="cube">
          <div className="cube__front">aaaaaaa</div>
          <div className="cube__back"></div>
          <div className="cube__top"></div>
          <div className="cube__bottom"></div>
          <div className="cube__left"></div>
          <div className="cube__right"></div>
        </div>
      </div>
    </div>
  );
}
