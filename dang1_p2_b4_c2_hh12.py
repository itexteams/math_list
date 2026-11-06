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


def bt_dang1_p2_b4_c2_hh12(self):
            # Khai báo biến
            # Hàm bổ trợ chuyển dấu chấm thành dấu phẩy cho số thập phân và làm tròn
            def fvn(number, precision=2):
                s = str(round(float(number), precision))
                if s.endswith('.0'):
                    s = s[:-2]
                return s.replace('.', ',')

            # --- PHẦN ĐIỀU CHỈNH LOGIC TOÁN HỌC ---
            while True:
                # Chọn vector chỉ phương (u1, u2, u3)
                ux = randint(8, 12)
                uy = randint(2, 6)
                uz = randint(4, 10)
                u_sq = ux**2 + uy**2 + uz**2

                # Để t=1 và t=2 là nghiệm, hình chiếu của O lên đường thẳng phải tại t = 1.5
                # Điều kiện: M.u + 1.5 * u^2 = 0
                xm_val = randint(-100, -60)
                ym_val = randint(-30, -10)

                tu_so = -1.5 * u_sq - xm_val*ux - ym_val*uy
                if tu_so % uz == 0: # Đảm bảo zm nguyên để số liệu đẹp
                    zm_val = int(tu_so // uz)
                    break

            # Gán lại các biến
            x_vtcp, y_vtcp, z_vtcp = ux, uy, uz
            xm, ym, zm = xm_val, ym_val, zm_val

            t = symbols('t')

            # Điểm A (t=1) và B (t=2) - Hai điểm này nằm trên mặt cầu quan sát
            xa, ya, za = xm + x_vtcp*1, ym + y_vtcp*1, zm + z_vtcp*1
            xb, yb, zb = xm + x_vtcp*2, ym + y_vtcp*2, zm + z_vtcp*2

            # Bán kính R và R^2 chính xác từ tọa độ (đảm bảo khớp phương trình)
            r2 = xa**2 + ya**2 + za**2
            r_val = math.sqrt(r2)
            do_cao_km = (r_val - 6.4) * 1000

            # Điểm M, N để tính tỉ lệ (M ứng với t=0, N ứng với t_n)
            t_n = randint(5, 8)
            xn, yn, zn = xm + x_vtcp*t_n, ym + y_vtcp*t_n, zm + z_vtcp*t_n

            # Các đại lượng tính toán
            ab = math.sqrt((xb - xa)**2 + (yb - ya)**2 + (zb - za)**2)
            pt = expand((xm + x_vtcp*t)**2 + (ym + y_vtcp*t)**2 + (zm + z_vtcp*t)**2 - r2, t)
            t0 = randint(5, 15) # Thời gian di chuyển trong vùng quan sát (phút)

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('\\immini{'
                            'Các thiên thạch có đường kính lớn hơn $140$ m và có thể lại gần Trái Đất ở khoảng cách nhỏ hơn $7\\,500\\,000$ km '
                            'được coi là những vật thể có khả năng va chạm gây nguy hiểm cho Trái Đất. Để theo dõi những thiên thạch này, người ta đã '
                            'thiết lập các trạm quan sát. Giả sử có một hệ thống quan sát có khả năng theo dõi các vật thể '
                            'ở độ cao không vượt quá $%s$ km so với mực nước biển. Coi Trái Đất là khối cầu có bán kính $6400$ km. Chọn hệ trục tọa '
                            'độ $Oxyz$ có gốc O tại tâm Trái Đất và đơn vị độ dài là $1000$ km. '
                            '}{'
                            r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.7,xscale=0.7]
