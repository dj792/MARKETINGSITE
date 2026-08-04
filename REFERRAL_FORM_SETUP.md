# Referral form → "Referral Submissions" tab

The referral form on `referral-submit.html` uses the **same** Google Apps Script
web app as the contact form (same `WEBHOOK_URL`, same spreadsheet). A hidden
field `formType=referral` tells the script to write to a separate
**Referral Submissions** tab instead of Contact Submissions.

You only need to update the Apps Script once — the web app URL stays the same, so
nothing on the website changes.

## Referral Submissions columns

Written in this order (the script creates the header row automatically on the
first submission):

`DateTimeAdded`, `Name`, `Email`, `Company`, `Role`, `Company Size`, `Phone`,
`Message`, `Source`, `ReferredByName`, `ReferredByEmail`, `ReferredByPhone`,
`Page URL`

## 1. Open the existing Apps Script

1. Open the Google Sheet the contact form already writes to.
2. **Extensions → Apps Script**.
3. Select all the code in `Code.gs` and delete it.
4. Paste in the full script below (it keeps the contact form working **and**
   adds referral handling), then save (`Cmd+S`).

```javascript
// Tabs. Created automatically if missing.
const CONTACT_SHEET  = 'Contact Submissions';
const REFERRAL_SHEET = 'Referral Submissions';

// Email to notify on new submissions. Set to '' to disable.
const NOTIFY_EMAIL = 'dj@1to100advisors.com';

function doPost(e) {
  try {
    const data = (e && e.parameter) || {};
    if ((data.formType || '').toLowerCase() === 'referral') {
      return handleReferral(data);
    }
    return handleContact(data);
  } catch (err) {
    return json({ status: 'error', message: err.toString() });
  }
}

function handleReferral(data) {
  const sheet = getSheet(REFERRAL_SHEET, [
    'DateTimeAdded', 'Name', 'Email', 'Company', 'Role', 'Company Size',
    'Phone', 'Message', 'Source', 'ReferredByName', 'ReferredByEmail',
    'ReferredByPhone', 'Page URL'
  ]);

  sheet.appendRow([
    new Date(),
    data.name || '',
    data.email || '',
    data.company || '',
    data.role || '',
    data.companySize || '',
    data.phone || '',
    data.message || '',
    data.source || '',
    data.referredByName || '',
    data.referredByEmail || '',
    data.referredByPhone || '',
    data.page || ''
  ]);

  if (NOTIFY_EMAIL) {
    try {
      MailApp.sendEmail({
        to: NOTIFY_EMAIL,
        subject: 'New referral from ' + (data.referredByName || 'Unknown'),
        replyTo: data.referredByEmail || NOTIFY_EMAIL,
        body:
          'REFERRED LEADER\n' +
          'Name: ' + (data.name || '') + '\n' +
          'Email: ' + (data.email || '') + '\n' +
          'Company: ' + (data.company || '') + '\n' +
          'Role: ' + (data.role || '') + '\n' +
          'Company Size: ' + (data.companySize || '') + '\n' +
          'Phone: ' + (data.phone || '') + '\n' +
          'Notes: ' + (data.message || '') + '\n\n' +
          'REFERRED BY\n' +
          'Name: ' + (data.referredByName || '') + '\n' +
          'Email: ' + (data.referredByEmail || '') + '\n' +
          'Phone: ' + (data.referredByPhone || '') + '\n\n' +
          'Source: ' + (data.source || '') + '\n' +
          'Page: ' + (data.page || '')
      });
    } catch (mailErr) { console.error('Email failed:', mailErr); }
  }

  return json({ status: 'ok' });
}

function handleContact(data) {
  const sheet = getSheet(CONTACT_SHEET, [
    'Timestamp', 'Name', 'Email', 'Company', 'Role', 'Company Size',
    'Phone', 'Message', 'Source', 'Referred By', 'Submitted At', 'Page URL'
  ]);

  sheet.appendRow([
    new Date(),
    data.name || '',
    data.email || '',
    data.company || '',
    data.role || '',
    data.companySize || '',
    data.phone || '',
    data.message || '',
    data.source || '',
    data.referredBy || '',
    data.submittedAt || '',
    data.page || ''
  ]);

  if (NOTIFY_EMAIL) {
    try {
      MailApp.sendEmail({
        to: NOTIFY_EMAIL,
        subject: 'New contact form submission from ' + (data.name || 'Unknown'),
        replyTo: data.email || NOTIFY_EMAIL,
        body:
          'Name: ' + (data.name || '') + '\n' +
          'Email: ' + (data.email || '') + '\n' +
          'Company: ' + (data.company || '') + '\n' +
          'Role: ' + (data.role || '') + '\n' +
          'Company Size: ' + (data.companySize || '') + '\n' +
          'Phone: ' + (data.phone || '') + '\n\n' +
          'Message:\n' + (data.message || '') + '\n\n' +
          'Source: ' + (data.source || '') + '\n' +
          'Referred By: ' + (data.referredBy || '') + '\n' +
          'Page: ' + (data.page || '')
      });
    } catch (mailErr) { console.error('Email failed:', mailErr); }
  }

  return json({ status: 'ok' });
}

// Get a tab by name, creating it (with a bold, frozen header row) if missing.
function getSheet(name, headers) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(name);
  if (!sheet) sheet = ss.insertSheet(name);
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(headers);
    sheet.getRange(1, 1, 1, headers.length).setFontWeight('bold');
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function json(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function doGet() {
  return ContentService.createTextOutput('1 to 100 Advisors form endpoint. POST only.');
}
```

## 2. Redeploy the web app (new version)

Code changes require publishing a new version:

1. **Deploy → Manage deployments**.
2. Click the **pencil (edit)** icon on the existing deployment.
3. **Version → New version**, then **Deploy**.

The web app URL does not change, so `referral-submit.html` (and `contact.html`)
already point to the right place.

> Already have a `Referral Submissions` tab with your headers? The script matches
> them by writing in the same order — you don't need to pre-create the tab, but if
> you did, make sure the header order matches the list above.

## 3. Test

1. Open `referral-submit.html` in a browser (after deploying the site).
2. Submit test data.
3. Confirm a new row appears in the **Referral Submissions** tab and (if
   `NOTIFY_EMAIL` is set) that you get the email.

If nothing appears, re-check that the deployment is **Execute as: Me** and
**Who has access: Anyone**, and that you published a **New version**.
