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


def bt_dang7_p2_b2_c2_hh12(self):
    # Khai báo biến
    x, y, z, t, k = symbols('x y z t k')

    while True:
        # VTCP và điểm đi qua của d1
        a1_d1 = random.choice([1, -1, 2, -2, 3, -3])
        b1_d1 = random.choice([1, -1, 2, -2, 3, -3])
        c1_d1 = random.choice([1, -1, 2, -2, 3, -3])
        x0_d1 = random.choice([0, 1, -1, 2, -2, 3, -3])
        y0_d1 = random.choice([0, 1, -1, 2, -2, 3, -3])
        z0_d1 = random.choice([0, 1, -1, 2, -2, 3, -3])

        # VTCP và điểm đi qua của d2
        a2_d2 = random.choice([1, -1, 2, -2, 3, -3])
        b2_d2 = random.choice([1, -1, 2, -2, 3, -3])
        c2_d2 = random.choice([1, -1, 2, -2, 3, -3])
        x0_d2 = random.choice([0, 1, -1, 2, -2, 3, -3])
        y0_d2 = random.choice([0, 1, -1, 2, -2, 3, -3])
        z0_d2 = random.choice([0, 1, -1, 2, -2, 3, -3])

        # Chọn tham số t1 cho A thuộc d1, t2 cho B thuộc d2
        t1 = 1
        t2 = -1

        A_x = x0_d1 + a1_d1 * t1
        A_y = y0_d1 + b1_d1 * t1
        A_z = z0_d1 + c1_d1 * t1

        B_x = x0_d2 + a2_d2 * t2
        B_y = y0_d2 + b2_d2 * t2
        B_z = z0_d2 + c2_d2 * t2

        # Đảm bảo A và B không trùng nhau
        if (A_x, A_y, A_z) == (B_x, B_y, B_z):
            continue

        # Đảm bảo d1 và d2 không cùng phương
        u1 = Matrix([a1_d1, b1_d1, c1_d1])
        u2 = Matrix([a2_d2, b2_d2, c2_d2])
        cross_u = [b1_d1 * c2_d2 - c1_d1 * b2_d2,
                   c1_d1 * a2_d2 - a1_d1 * c2_d2,
                   a1_d1 * b2_d2 - b1_d1 * a2_d2]
        if cross_u == [0, 0, 0]:
            continue

        # Để A, M, B thẳng hàng: chọn M là trung điểm AB (hoặc M chia đoạn AB)
        # Chọn M nguyên: kiểm tra tính chẵn lẻ để M có tọa độ nguyên đẹp
        if (A_x + B_x) % 2 == 0 and (A_y + B_y) % 2 == 0 and (A_z + B_z) % 2 == 0:
            Mx = (A_x + B_x) // 2
            My = (A_y + B_y) // 2
            Mz = (A_z + B_z) // 2
            # Tránh trường hợp M trùng A hoặc B
            if (Mx, My, Mz) != (A_x, A_y, A_z):
                break

    # Nội dung câu hỏi (chú ý sửa \frac{y+%s}{%s} thành \frac{y-%s}{%s})
    noidungcauhoi = ('''Trong không gian $Oxyz$, cho điểm $M(%s;%s;%s)$ và hai đường thẳng 
