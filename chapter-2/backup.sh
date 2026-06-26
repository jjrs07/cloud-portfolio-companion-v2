#!/bin/bash
# Production-grade backup script using local syslog logging
BUCKET_NAME="your-backup-bucket-name"
BACKUP_DIR="/var/www/html" # Directory containing web code
TIMESTAMP=$(date +%Y-%m-%d-%H%M%S)
BACKUP_FILE="/tmp/web-backup-${TIMESTAMP}.tar.gz"

echo "Starting backup of ${BACKUP_DIR}..."

# Verify S3 connectivity
if ! aws s3 ls "s3://${BUCKET_NAME}" > /dev/null 2>&1; then
    echo "Error: Cannot access S3 bucket ${BUCKET_NAME}. Check IAM Role." >&2
    exit 1
fi

# Create archive
tar -czf "${BACKUP_FILE}" -C "${BACKUP_DIR}" . 2>/dev/null

# Upload and log results
if aws s3 cp "${BACKUP_FILE}" "s3://${BUCKET_NAME}/backups/"; then
    logger -t "BACKUP_SYSTEM" "Success: Uploaded web backup to S3."
    rm -f "${BACKUP_FILE}"
    echo "Backup completed successfully."
else
    logger -t "BACKUP_SYSTEM" "Error: S3 backup upload failed."
    rm -f "${BACKUP_FILE}"
    exit 1
fi