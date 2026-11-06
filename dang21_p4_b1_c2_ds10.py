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


def bt_dang21_p4_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random bài toán
                # Chọn hệ số nhân (10 nghìn hoặc 20 nghìn)
                factor = random.choice([10, 20])

                # Chọn đơn giá cơ sở (nguyên tố cùng nhau và khác nhau để hệ số sau rút gọn đẹp)
                pizza_raw = random.randint(3, 6)
                trasua_raw = random.randint(2, 5)
                while math.gcd(pizza_raw, trasua_raw) != 1 or pizza_raw == trasua_raw:
                    trasua_raw = random.randint(2, 5)

                limit_raw = random.randint(30, 60)

                gia_pizza = pizza_raw * factor
                gia_trasua = trasua_raw * factor
                tong_tien = limit_raw * factor

                hso_x = pizza_raw
                hso_y = trasua_raw
                hso_vp = limit_raw

                # Các đáp án trắc nghiệm
                da = '$%sx + %sy \\le %s$' % (latex(hso_x), latex(hso_y), latex(hso_vp))

                # Bước 4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = [
                    '$%sx + %sy > %s$' % (latex(hso_x), latex(hso_y), latex(hso_vp)),
                    '$%sx + %sy \\ge %s$' % (latex(hso_x), latex(hso_y), latex(hso_vp)),
                    '$%sx + %sy < %s$' % (latex(hso_x), latex(hso_y), latex(hso_vp)),
                    '$x + y \\le \\frac{%s}{%s}$' % (latex(hso_vp), latex(hso_x + hso_y)),
                    '$%sx + %sy \\le %s$' % (latex(hso_y), latex(hso_x), latex(hso_vp)),
                ]
                # Lọc bỏ nếu vô tình trùng với đáp án đúng
                s = [item for item in s if item != da]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Bước 2: Viết lại đề bài
                noidungcauhoi = (
                    '''Sau trận cuối cùng của một mùa giải bóng đá nữ trường THPT A, huấn luyện viên trưởng đội lớp 10B dẫn cả đội vào cửa hàng Pizza - Trà sữa. Mỗi cái bánh Pizza có giá $%s$ nghìn đồng, một ly trà sữa có giá $%s$ nghìn đồng. Huấn luyện viên trưởng không muốn trả quá $%s$ nghìn đồng. Hãy lập bất phương trình mô tả tốt cho tình huống trên (với $x$ là số bánh Pizza và $y$ là số ly trà sữa).'''
                    % (latex(gia_pizza), latex(gia_trasua), latex(tong_tien))
                )

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bước 2: Viết lại lời giải
                loigiai = (
                    '''Với $x$ là số bánh Pizza và $y$ là số ly trà sữa thì: \\\\
            + Giá tiền của $x$ cái bánh Pizza là $%sx$ nghìn đồng. \\\\
            + Giá tiền của $y$ ly trà sữa là $%sy$ nghìn đồng. \\\\
            Tổng số tiền cần thanh toán là: $%sx + %sy$ nghìn đồng. \\\\
            Vì huấn luyện viên trưởng không muốn trả quá $%s$ nghìn đồng nên ta có bất phương trình $%sx + %sy \\le %s \\Leftrightarrow %sx + %sy \\le %s$.'''
                    % (
                        latex(gia_pizza), latex(gia_trasua), latex(gia_pizza),
                        latex(gia_trasua), latex(tong_tien), latex(gia_pizza),
                        latex(gia_trasua), latex(tong_tien), latex(hso_x),
                        latex(hso_y), latex(hso_vp)
                    )
                )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

