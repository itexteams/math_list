import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang6_p1_b5_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Câu hỏi về tính chất của phép chiếu song song
        # Nội dung câu hỏi
        cau_hoi_str = "Trong các mệnh đề sau, mệnh đề nào đúng?"
        noidungcauhoi = "%s" % (cau_hoi_str)

        # Đáp án đúng
        du = [
            "Phép chiếu song song biến một tam giác thành một tam giác nếu mặt phẳng chứa tam giác không cùng phương với phương chiếu"
        ]
        da = random.choice(du)

        # Các đáp án sai
        s = [
            "Hình chiếu song song của hai đường thẳng cắt nhau là hai đường thẳng song song",
            "Hình chiếu song song của một hình bình hành là một hình bình hành",
            "Phép chiếu song song không làm thay đổi tỉ số độ dài của hai đoạn thẳng",
            "Hình chiếu song song của hai đường thẳng chéo nhau luôn là hai đường thẳng song song",
            "Phép chiếu song song biến một đoạn thẳng luôn thành một đoạn thẳng có độ dài bằng nó"
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Các phương án
        da_d = "\\True " + str(da)
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Lời giải chi tiết
        loigiai_str = (
            "Xét tính đúng, sai của từng mệnh đề theo tính chất của phép chiếu song song:\\\\"
            "+ Mệnh đề \"Hình chiếu song song của hai đường thẳng cắt nhau là hai đường thẳng song song\" là sai vì hình chiếu song song của hai đường thẳng cắt nhau là hai đường thẳng cắt nhau (hoặc trùng nhau nếu mặt phẳng chứa hai đường thẳng đó song song hoặc chứa phương chiếu).\\\\"
            "+ Mệnh đề \"Hình chiếu song song của một hình bình hành là một hình bình hành\" là sai vì nếu mặt phẳng chứa hình bình hành song song hoặc chứa phương chiếu thì hình chiếu của nó là một đoạn thẳng.\\\\"
            "+ Mệnh đề \"Phép chiếu song song không làm thay đổi tỉ số độ dài của hai đoạn thẳng\" là sai vì phép chiếu song song chỉ bảo toàn tỉ số độ dài của hai đoạn thẳng khi hai đoạn thẳng đó cùng nằm trên một đường thẳng hoặc nằm trên hai đường thẳng song song.\\\\"
            "+ Mệnh đề \"Phép chiếu song song biến một tam giác thành một tam giác nếu mặt phẳng chứa tam giác không cùng phương với phương chiếu\" là đúng theo tính chất cơ bản của phép chiếu song song.\\\\"
            "Vậy mệnh đề đúng là: \"Phép chiếu song song biến một tam giác thành một tam giác nếu mặt phẳng chứa tam giác không cùng phương với phương chiếu\"."
        )
        loigiai = "%s" % (loigiai_str)

    # Xuất câu trắc nghiệm
    content = (
        '\\begin{minipage}{\\textwidth}\n'
        '\\begin{ex}\n' +
        str(noidungcauhoi) + '\n'
        '\\choice\n'
        '{' + str(list_1[0]) + '}\n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n'
        '\\end{minipage}\n\n')
    return content

