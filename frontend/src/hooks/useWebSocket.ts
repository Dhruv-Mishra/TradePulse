import { useEffect, useState } from "react";
import { parseBlockDeals } from "../api/adapter";

export function useWebSocketData(url: string) { //TODO: Have a strict URL type and error handling
  const [data, setData] = useState([]);

  useEffect(() => {
    const socket = new WebSocket(url);

    socket.onmessage = (event) => {
      const raw = JSON.parse(event.data);
      setData(parseBlockDeals(raw));
    };

    socket.onclose = () => {
      console.log("WebSocket closed. Reconnecting...");
      setTimeout(() => useWebSocketData(url), 3000); // auto-reconnect
    };

    return () => socket.close();
  }, [url]);

  return data;
}
