(() => {
  'use strict';
  const reveal = document.getElementById('reveal-email');
  const contact = document.getElementById('email-contact');
  const link = document.getElementById('email-link');
  const copy = document.getElementById('copy-email');
  const status = document.getElementById('contact-status');
  if (!reveal || !contact || !link || !copy || !status) return;

  // Decode only after a visitor explicitly requests the contact address.
  // This discourages simple harvesters; it is not a security boundary.
  const payload = [31, 46, 41, 32, 62, 50, 105, 4, 47, 34, 41, 106, 127, 7, 52, 51, 50, 35, 34, 41, 51, 105, 50, 51, 52, 105, 34, 35, 50, 105, 38, 50];
  let address = '';
  reveal.hidden = false;
  reveal.addEventListener('click', () => {
    address = String.fromCharCode(...payload.map(value => value ^ 71));
    link.textContent = address;
    link.href = 'mailto:' + address;
    link.setAttribute('aria-label', 'Email Xingyu Chen');
    contact.hidden = false;
    reveal.setAttribute('aria-expanded', 'true');
    reveal.hidden = true;
    link.focus();
  }, { once: true });

  copy.addEventListener('click', async () => {
    if (!address) return;
    try {
      await navigator.clipboard.writeText(address);
      status.textContent = 'Email copied.';
    } catch {
      status.textContent = 'Select and copy the address above.';
    }
  });
})();
