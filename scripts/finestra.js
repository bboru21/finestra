(function() {
  "use strict";
	
	// begin browser feature detection methods
	//function supports_video() {
	//	return !!PLAYER.canPlayType;
	//}

	//function supports_h264_baseline_video() {
	//	if (!supports_video()) { return false;  }
	//	return PLAYER.canPlayType('video/mp4; codecs="avc1.42E01E, mp4a.40.2"');
	//}

	//function supports_ogg_theora_video() {
	//	if (!supports_video()) { return false; }
	//	return PLAYER.canPlayType('video/ogg; codecs="theora, vorbis"');
	//}
	// end browser feature detection methods
	
	window.Finestra = function(options) {
		
		this.start_time = new Date().getTime();
		
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
		var containerId = options.containerId || "videoPlayerContainer_" + this.start_time;
		this.container = document.getElementById(containerId);
		if (!this.container) {
			this.container = document.createElement("div");
			this.container.setAttribute("id", containerId);
			document.getElementsByTagName("body")[0].appendChild(this.container);
		}
		this.container.style.height = this.height;
		this.container.style.width = this.width;
		
		// player
		this.player = document.createElement("video");
		this.player.setAttribute("controls", "controls");
		this.player.setAttribute("width", "100%");
		this.player.setAttribute("height", "100%");
		if (this.autoplay) { this.player.setAttribute("autoplay", "autoplay"); }
		
		// poster image
		this.poster = options.poster || null;
		if (!!this.poster) { this.player.setAttribute("poster", this.poster); }
		
		// begin source tag logic
		this.source = options.source || {};
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
		// end source tag logic
		
		this.container.appendChild(this.player);
	};
	
	Finestra.prototype.play = function() {
		this.player.play();
	};
	
	Finestra.prototype.pause = function() {
		this.player.pause();
	};

}());
