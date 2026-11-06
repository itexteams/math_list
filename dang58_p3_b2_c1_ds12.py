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


def bt_dang58_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số cho bài toán
                # a: hệ số của x, x0: số lượng máy chủ tối ưu, c: hệ số tự do
                a = random.randint(4, 10)
                x0 = random.randint(20, 50)
                c = random.randint(2020, 2030)

                # Tính b để x0 là điểm cực trị: T'(x) = a - b/x^2 = 0 => b = a * x0^2
                b = a * (x0**2)

                # Tính độ trễ tối thiểu (T_min)
                t_min = 2 * a * x0 + c

                kq_x = x0
                kq_t = t_min

                # Đáp án đúng
                du = ['$%s$ máy chủ, $%s$ ms' % (kq_x, kq_t)]
                da = random.choice(du)

                # Các đáp án trắc nghiệm sai (distractors)
                # Đảm bảo không trùng với đáp án đúng
                s = [
                    '$%s$ máy chủ, $%s$ ms' % (kq_x + 1, t_min + a),
                    '$%s$ máy chủ, $%s$ ms' % (kq_x - 1, t_min - a),
                    '$%s$ máy chủ, $%s$ ms' % (kq_x + 2, t_min + 5),
                    '$%s$ máy chủ, $%s$ ms' % (kq_x, t_min + 50),
                    '$%s$ máy chủ, $%s$ ms' % (kq_x - 2, t_min + 15),
                    '$%s$ máy chủ, $%s$ ms' % (kq_x + 5, t_min - 20)
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Vào một ngày khai mở nền tảng thi trắc nghiệm trực tuyến, hệ thống áp dụng thuật toán phân luồng mới để giảm thiểu tối đa độ trễ. Theo tài liệu kỹ thuật, độ trễ trung bình $T$ (tính bằng mili-giây) phụ thuộc vào số lượng máy chủ ảo $x$ được kích hoạt đồng thời ($x > 0, x \\in \\mathbb{R}$). Hàm số mô phỏng độ trễ được các kỹ sư thiết lập như sau:
                $$T(x) = %sx + \\frac{%s}{x} + %s$$
                Sử dụng công cụ đạo hàm, hãy khảo sát hàm số trên để tìm số lượng máy chủ ảo $x$ cần thiết lập sao cho độ trễ của hệ thống đạt mức nhỏ nhất. Độ trễ tối thiểu đó bằng bao nhiêu?'''
                                 % (a, b, c))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Hàm số độ trễ: 
                $$T(x) = %sx + \\frac{%s}{x} + %s$$
                Tập xác định: $D = (0, +\\infty)$ (do số lượng máy chủ phải lớn hơn 0). \\\\
                Ta tính đạo hàm bậc nhất của hàm số:
                $$T'(x) = %s - \\frac{%s}{x^2}$$
                Cho $T'(x) = 0$ để tìm các điểm mà tại đó độ trễ có thể đạt cực trị:
                $$%s - \\frac{%s}{x^2} = 0 \\Leftrightarrow %sx^2 = %s \\Leftrightarrow x^2 = %s$$
                Lấy căn bậc hai hai vế, do điều kiện $x > 0$, ta có:
                $$x = %s$$
                Để khẳng định đây là điểm làm cho hàm số đạt giá trị nhỏ nhất, ta xét đạo hàm bậc 2:
                $$T''(x) = \\frac{%s}{x^3}$$
                Với mọi $x > 0$, ta luôn có $T''(x) > 0$. \\\\
                Vì đạo hàm bậc hai luôn dương, đồ thị hàm số lõm xuống dưới trên toàn bộ khoảng $(0, +\\infty)$. Do đó, điểm tới hạn $x = %s$ chắc chắn là điểm cực tiểu và cũng là giá trị nhỏ nhất tuyệt đối. \\\\
                Thay $x = %s$ vào hàm số ban đầu để tìm độ trễ tối thiểu:
                $$T(%s) = %s(%s) + \\frac{%s}{%s} + %s = %s + %s + %s = %s \\text{ (ms)}$$
                Kết luận thực tiễn: Cần cấu hình kích hoạt chính xác $%s$ máy chủ ảo để hệ thống đạt độ trễ thấp nhất là $%s$ ms.'''
                           % (a, b, c, 
                              a, b, 
                              a, b, a, b, x0**2, 
                              x0, 
                              2*b, 
                              x0, 
                              x0, 
                              x0, a, x0, b, x0, c, a*x0, a*x0, c, t_min, 
                              x0, t_min))
                dapan='\\shortans[0]{$%s$}\n'%(t_min)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

