FROM webdevops/liquibase:postgres

USER root

WORKDIR /liquibase

COPY ./docker/entripoints/migrator.sh .
RUN chmod +x ./migrator.sh

COPY ./backend/project/models/changeLog .

ENTRYPOINT ["./migrator.sh"]

CMD ["update"]
