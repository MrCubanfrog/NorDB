/*
+--------------------------+
|NORDIC EVENT ROOT POLICIES|
+--------------------------+

This file contains the sql commands for creating the correct policies for nordic event roots.

*/

/*
ADMIN POLICIES
--------------
*/

--Admin policy. Allow admins to access all operations freely.
CREATE POLICY admin_all_policy ON nordic_event_root FOR ALL TO admins USING (true) WITH CHECK (true);

/*
DEFAULT USER POLICIES
---------------------
*/

--Default user view policy. Allow users to select all event roots which have secure or public events in them
CREATE POLICY user_view_policy ON nordic_event_root FOR SELECT TO default_users 
    USING   (
            'public' IN (SELECT privacy_setting from nordic_event, creation_info WHERE nordic_event.root_id = nordic_event_root.id AND nordic_event.creation_id = creation_info.id) OR
            'secure' IN (SELECT privacy_setting from nordic_event, creation_info WHERE nordic_event.root_id = nordic_event_root.id AND nordic_event.creation_id = creation_info.id) OR
            'private' IN (SELECT privacy_setting from nordic_event, creation_info WHERE nordic_event.root_id = nordic_event_root.id AND nordic_event.creation_id = creation_info.id AND owner = current_user) OR
	    0 = (SELECT COUNT(*) FROM nordic_event WHERE nordic_event.root_id = nordic_event_root.id)
            );

--Default user insert policy. Allow users to insert event roots freely.
CREATE POLICY user_insert_policy ON nordic_event_root FOR INSERT TO default_users WITH CHECK (true);

--Default user delete policy. Allow users to delete empty root id's.
CREATE POLICY user_delete_policy ON nordic_event_root FOR DELETE TO default_users 
    USING   (
            0 = (SELECT COUNT(*) FROM nordic_event WHERE nordic_event.root_id = nordic_event_root.id)
            );

/*
GUEST POLICIES
--------------
*/

--Guest select policy. Allow Guests to see all root ids with public events
CREATE POLICY guest_select_policy ON nordic_event_root FOR SELECT TO guests
    USING   (
            'public' IN (SELECT privacy_setting from nordic_event, creation_info WHERE nordic_event.root_id = nordic_event_root.id AND nordic_event.creation_id = creation_info.id)
            );
