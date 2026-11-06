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


def bt_dang35_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- BƯỚC 1: TẠO THAM SỐ ---
            m_fixed = random.choice([-2, -1, 1, 2]) 
            k_val = random.randint(2, 5) 

            # --- NỘI DUNG CÂU HỎI ---
            # Không dùng tiền tố r ở đây theo yêu cầu
            noidungcauhoi = "Cho hàm số $f(x)=|x+m|$."

            ########################################################################
            # Nhận biết (Ý a)
            ########################################################################
            nb_da_1_d = "\\True Khi $m=%s$, hàm số $g(x)=|x-1|+|x+3|$ trên $(-2025; -5)$ nghịch biến" % (m_fixed)
            nb_da_1_s = "Khi $m=%s$, hàm số $g(x)=|x-1|+|x+3|$ trên $(-2025; -5)$ đồng biến" % (m_fixed)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ("Khi $m=%s$, hàm số $g(x)=|x-1|+|x+3|$ trên $(-2025; -5)$ có dạng: $g(x)=-x+1-x-3 = -2x-2$ nên hàm số nghịch biến." % (m_fixed))

            ########################################################################
            # Thông hiểu (Ý b)
            ########################################################################
            th_da_1_d = "\\True Khi $m=%s$, hàm số $g(x)=|x-1|+|x+3|$ đạt giá trị nhỏ nhất bằng $4$ tại mọi $x \\in [-3; 1]$" % (m_fixed)
            th_da_1_s = "Khi $m=%s$, hàm số $g(x)=|x-1|+|x+3|$ đạt giá trị nhỏ nhất bằng $0$ tại $x=1$" % (m_fixed)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ("Khi $m=%s$, hàm số $g(x)=|x-1|+|x+3| = \\begin{cases} -2x-2, x < -3 \\\\ 4, -3 \\le x \\le 1 \\\\ 2x+2, x > 1 \\end{cases}$. \\\\ Hàm số đạt giá trị nhỏ nhất là $4$ khi $x \\in [-3; 1]$. \\\\ Vì $x$ nguyên nên có $5$ giá trị của $x$ là $-3; -2; -1; 0; 1$." % (m_fixed))

            ########################################################################
            # Vận dụng (Ý c)
            ########################################################################
            vd_da_1_d = "\\True Miền giá trị của hàm số $f(x)=|x-1|+2$ trên đoạn $[-1; 3]$ là $T=[2; 4]$. Suy ra $a+b=6$"
            vd_da_1_s = "Miền giá trị của hàm số $f(x)=|x-1|+2$ trên đoạn $[-1; 3]$ là $T=[0; 2]$. Suy ra $a+b=2$"
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ("Khi $m=%s$, $f(x)=|x-1|$. \\\\ Ta có $-2 \\le x-1 \\le 2, \\forall x \\in [-1; 3] \\Leftrightarrow 0 \\le |x-1| \\le 2, \\forall x \\in [-1; 3] \\Leftrightarrow 2 \\le |x-1|+2 \\le 4$. \\\\ Suy ra miền giá trị của hàm số trên đoạn $[-1; 3]$ là $T=[2; 4]$. \\\\ Vậy $a+b=6$." % (m_fixed))

            ########################################################################
            # Vận dụng cao (Ý d)
            ########################################################################
            m1 = k_val
            m2 = -k_val - 2
            tong_m = m1 + m2

            vdc_da_1_d = "\\True Tổng các giá trị thực của $m$ để $\\min_{[0; 2]} |x+m| = %s$ là %s" % (k_val, tong_m)
            vdc_da_1_s = "Tổng các giá trị thực của $m$ để $\\min_{[0; 2]} |x+m| = %s$ là %s" % (k_val, k_val)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ("Với $\\forall x \\in [0; 2]$ ta có $m \\le x+m \\le 2+m$. \\\\ Do đó nếu $-m \\in [0; 2]$ thì $|x+m|$ đạt giá trị nhỏ nhất là $0$; nếu $-m \\notin [0; 2]$ thì $|x+m|$ đạt giá trị nhỏ nhất là $\\min \\{|m|; |2+m|\\}$. \\\\ Yêu cầu bài toán trở thành tìm $m$ sao cho $\\min \\{|m|; |2+m|\\} = %s$. \\\\ Trường hợp 1: $\\begin{cases} |m| = %s \\\\ |2+m| \\ge %s \\end{cases} \\Leftrightarrow m = %s$. \\\\ Trường hợp 2: $\\begin{cases} |m| \\ge %s \\\\ |2+m| = %s \\end{cases} \\Leftrightarrow m = %s$. \\\\ Do đó giá trị $m$ thỏa mãn bài toán là $m = %s$ và $m = %s$. \\\\ Vậy tổng các giá trị của $m$ là %s." 
            % (k_val, k_val, k_val, m1, k_val, k_val, m2, m1, m2, tong_m))

            # --- CHỌN ĐÁP ÁN ĐÚNG/SAI ---
            def count_true(ans_list):
                return sum(1 for x in ans_list if "\\True" in x)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)
                if 1 <= count_true([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # --- XUẤT KẾT QUẢ ---
            # Sử dụng dấu ngoặc đơn để bọc toàn bộ chuỗi nối, tránh mất mát dữ liệu
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" +
                noidungcauhoi + "\n" +
                "\\choiceTFn \n"
                "{" + ans_a + "}\n"
                "{" + ans_b + "}\n"
                "{" + ans_c + "}\n"
                "{" + ans_d + "}\n"
                "\\loigiai{ \n"
                "\\begin{enumEX}[a)]{1} \n"
                "\\item " + loigiai_nb_1 + "\n"
                "\\item " + loigiai_th_1 + "\n"
                "\\item " + loigiai_vd_1 + "\n"
                "\\item " + loigiai_vdc_1 + "\n"
                "\\end{enumEX}} \n"
                "\\end{ex}\n"
                "\\end{minipage} \n\n")
            return content


