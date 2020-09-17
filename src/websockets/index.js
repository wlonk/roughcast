/*
# @@@ WEBSOCKETS
import Sockette from 'sockette';


export const createSocket = ({ url, options = {}, dispatch }) => {
  if (!(url && dispatch)) {
    return null;
  }
  const defaults = {
    timeout: 1000,
    maxAttempts: Infinity,
    onopen: (e) => {},
    onmessage: (e) => {},
    onreconnect: (e) => {},
    onmaximum: (e) => {},
    onclose: (e) => {},
    onerror: (e) => {},
  };
  const opts = { ...defaults, ...options };

  let open = false;
  let lostConnection = false;
  const pending = new Set();

  const socket = new Sockette(url, {
    timeout: opts.timeout,
    maxAttempts: opts.maxAttempts,
    onopen: (e) => {
      dispatch(connectSocket());
      open = true;
      for (const payload of pending) {
        log('[WebSocket] subscribing to:', payload);
        socket.json(payload);
      }
      pending.clear();
      if (lostConnection) {
        lostConnection = false;
        log('[WebSocket] reconnected');
        opts.onreconnect(e);
      } else {
        log('[WebSocket] connected');
        opts.onopen(e);
      }
    },
    onmessage: (e) => {
      let data = e.data;
      try {
        data = JSON.parse(e.data);
      } catch (err) {
        // swallow error
      }
      log('[WebSocket] received:', data);
      const action = getAction(data);
      if (action) {
        dispatch(action);
      }
      opts.onmessage(e);
    },
    onreconnect: () => {
      log('[WebSocket] attempting to reconnect…');
      if (!lostConnection) {
        lostConnection = true;
      }
    },
    onmaximum: (e) => {
      log(`[WebSocket] ending reconnect after ${opts.maxAttempts} attempts`);
      opts.onmaximum(e);
    },
    onclose: (e) => {
      log('[WebSocket] closed');
      if (open) {
        open = false;
        setTimeout(() => {
          if (!open) {
            dispatch(disconnectSocket());
          }
        }, 5000);
      }
      opts.onclose(e);
    },
    onerror: (e) => {
      log('[WebSocket] error');
      opts.onerror(e);
    },
  });

  const subscribe = (data: Subscription) => {
    const payload = { ...data, action: WEBSOCKET_ACTIONS.SUBSCRIBE };
    if (open) {
      log('[WebSocket] subscribing to:', payload);
      socket.json(payload);
    } else {
      pending.add(payload);
    }
  };

  const unsubscribe = (data: Subscription) => {
    const payload = { ...data, action: WEBSOCKET_ACTIONS.UNSUBSCRIBE };
    if (open) {
      log('[WebSocket] unsubscribing from:', payload);
      socket.json(payload);
    } else {
      pending.add(payload);
    }
  };

  let reconnecting: NodeJS.Timeout | undefined;
  const clearReconnect = () => {
    if (reconnecting) {
      clearInterval(reconnecting);
      reconnecting = undefined;
    }
  };

  const reconnect = () => {
    socket.close(1000, 'user logged out');
    // Without polling, the `onopen` callback after reconnect could fire before
    // the `onclose` callback...
    reconnecting = setInterval(() => {
      if (!open) {
        socket.open();
        clearReconnect();
      }
    }, 500);
  };

  return {
    subscribe,
    unsubscribe,
    reconnect,
  };
};
*/
