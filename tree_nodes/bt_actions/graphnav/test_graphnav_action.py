""""Spot GraphNav actions test."""

from __future__ import annotations

from py_trees.behaviour import Behaviour
from py_trees.blackboard import Client
from py_trees.common import Access
from py_trees.common import Status

from rclpy.action import ActionClient
from rclpy.action.server import ServerGoalHandle
from rclpy.node import Node
from rclpy.task import Future

from spot_bt_ros_msgs.action import PlanSpotBodyTask

from spot_bt_ros_py.utils import SpotBTActionClientMixin


class UploadGraphNavGraph(Behaviour, SpotBTActionClientMixin):


class LocalizeToWaypointInGraphNav(Behaviour, SpotBTActionClientMixin):


class NavigateToWaypointInGraphNav(Behaviour, SpotBTActionClientMixin):