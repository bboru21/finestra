(function() {
  "use strict";
	
	window.Finestra = function(options) {
		
		var addPx = function(val) {
			if (!isNaN(val)) { val += "px"; }
			return val;
		}
		
		var options = options || {};

		this.autoplay = options.autoplay || false;
		this.height = addPx(options.height) || "324px";
		this.player_embedded = false;
		this.width = addPx(options.width) || "576px";
		
		// container
		this.container = document.createElement("div");
		this.container.style.height = this.height;
		this.container.style.width = this.width;
		
		// player
		this.player = document.createElement("video");
		this.player.setAttribute("controls", "controls");
		this.player.setAttribute("width", "100%");
		this.player.setAttribute("height", "100%");
		if (this.autoplay) { this.player.setAttribute("autoplay", "autoplay"); }
		this.container.appendChild(this.player);
	
	};
	
	Finestra.prototype.play = function(options) {
		
		var options = options || {};
		
		this.poster = options.poster || null;
		this.source = options.source || {};
		
		if (!!this.poster) { this.player.setAttribute("poster", this.poster); }

		if (typeof this.source.mp4 === "string") {
			var mp4Source = document.createElement("source");
			mp4Source.setAttribute("src", this.source.mp4 );
			mp4Source.setAttribute("type", "video/mp4; codecs=avc1.42E01E, mp4a.40.2");
			this.player.appendChild(mp4Source);
		} 
		
		if (typeof this.source.webm === "string") {
			var webmSource = document.createElement("source");
			webmSource.setAttribute("src", this.source.webm);
			webmSource.setAttribute("type", "video/webm; codecs=vp8, vorbis");
			this.player.appendChild(webmSource);
		}
		
		if (typeof this.source.ogv === "string") {
			var ogvSource = document.createElement("source");
			ogvSource.setAttribute("src",  this.source.ogv);
			ogvSource.setAttribute("type", "video/ogg; codecs=theora, vorbis");
			this.player.appendChild(ogvSource);
		}
		
		if (!this.player_embedded) {
			this.player_embedded = true;
			document.getElementsByTagName("body")[0].appendChild(this.container);
		}
	};
	
}());
