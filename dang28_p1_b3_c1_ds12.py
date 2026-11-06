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


def bt_dang28_p1_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các giá trị x cho bảng biến thiên (đảm bảo x1 < x2 < x3)
                x1 = randint(-3, -1)
                x2 = x1 + randint(1, 2)
                x3 = x2 + randint(1, 2)

                # Random các giới hạn tại vô cực (Tiệm cận ngang)
                # y_lim_neg: giới hạn tại -vô cực
                # y_lim_pos: giới hạn tại +vô cực
                y_lim_neg = randint(-5, -2)
                y_lim_pos = randint(-3, 2)

                # Số lượng TCN (tối đa 2)
                num_tcn = 0
                tcn_set = set()
                if y_lim_neg is not None:
                    tcn_set.add(y_lim_neg)
                if y_lim_pos is not None:
                     tcn_set.add(y_lim_pos)
                num_tcn = len(tcn_set)

                # Các giới hạn tại x1, x2, x3 để xác định TCĐ
                # Theo đề mẫu: tại x1 có TCĐ, tại x3 có TCĐ, tại x2 có cực đại (không phải TCĐ)
                # Ta sẽ giữ nguyên cấu trúc giới hạn này để đảm bảo có 2 TCĐ.
                num_tcd = 2

                # Cực trị tại x2
                y_cuc_dai = randint(1, 5)

                # Tổng số tiệm cận
                tong_tc = num_tcn + num_tcd

                # Chuyển đổi định dạng latex
                str_x1 = latex(x1)
                str_x2 = latex(x2)
                str_x3 = latex(x3)
                str_y_lim_neg = latex(y_lim_neg)
                str_y_lim_pos = latex(y_lim_pos)
                str_y_cuc_dai = latex(y_cuc_dai)
                str_tong_tc = latex(tong_tc)

                # Đáp án đúng
                da = '$%s$' % str_tong_tc

                # Phương án nhiễu
                options = [1, 2, 3, 4, 5, 6]
                if tong_tc in options:
                    options.remove(tong_tc)

                s = ['$%s$' % latex(opt) for opt in random.sample(options, 3)]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Code TikZ vẽ Bảng biến thiên (Có khung bao)
                bang_bien_thien = ('''\\begin{center}
            \\begin{tikzpicture}[line width=1pt]
            \\draw (0,0) rectangle (14,3.2);
            \\draw (0,2.4) -- (14,2.4);
            \\draw (0,1.6) -- (14,1.6);
            \\draw (1,0) -- (1,3.2);
            \\node at (0.5, 2.8) {$x$};
            \\node at (0.5, 2.0) {$y'$};
            \\node at (0.5, 0.8) {$y$};
            \\node at (1.5, 2.8) {$-\\infty$};
            \\node at (4.5, 2.8) {$%s$};
            \\node at (7.5, 2.8) {$%s$};
            \\node at (10.5, 2.8) {$%s$};
            \\node at (13.0, 2.8) {$+\\infty$};
            \\node at (2.8, 2.0) {$+$};
            \\node at (6.0, 2.0) {$+$};
            \\node at (7.5, 2.0) {$||$};
            \\node at (9.0, 2.0) {$-$};
            \\node at (11.8, 2.0) {$+$};
            \\draw (4.4, 0) -- (4.4, 2.4);
            \\draw (4.6, 0) -- (4.6, 2.4);
            \\draw (10.4, 0) -- (10.4, 2.4);
            \\draw (10.6, 0) -- (10.6, 2.4);
            \\node at (1.5, 0.5) {$%s$};
            \\node at (4.0, 1.3) {$+\\infty$};
            \\draw[->] (1.8, 0.6) -- (3.7, 1.2);
            \\node at (5.0, 0.3) {$-\\infty$};
            \\node at (7.5, 1.3) {$%s$};
            \\node at (10.0, 0.3) {$-\\infty$};
            \\draw[->] (5.4, 0.4) -- (7.2, 1.2);
            \\draw[->] (7.8, 1.2) -- (9.6, 0.4);
            \\node at (11.0, 0.3) {$-\\infty$};
            \\node at (13.0, 0.8) {$%s$};
            \\draw[->] (11.4, 0.4) -- (12.6, 0.7);
            \\end{tikzpicture}
            \\end{center}''' % (str_x1, str_x2, str_x3, str_y_lim_neg, str_y_cuc_dai, str_y_lim_pos))

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=f(x)$ có bảng biến thiên như hình sau
            %s
            Tổng số đường tiệm cận ngang và tiệm cận đứng của đồ thị hàm số $y=f(x)$ là''' % (bang_bien_thien))

                # Xử lý các đáp án vào danh sách
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tạo chuỗi liệt kê TCN cho lời giải
                tcn_str = []
                if y_lim_neg is not None:
                    tcn_str.append(f"$\\lim\\limits_{{x \\to -\\infty}} f(x) = {str_y_lim_neg} \\Rightarrow y = {str_y_lim_neg}$")
                if y_lim_pos is not None:
                    if y_lim_pos != y_lim_neg:
                        tcn_str.append(f"$\\lim\\limits_{{x \\to +\\infty}} f(x) = {str_y_lim_pos} \\Rightarrow y = {str_y_lim_pos}$")
                    else:
                         tcn_str.append(f"$\\lim\\limits_{{x \\to +\\infty}} f(x) = {str_y_lim_pos}$ (trùng với TCN ở trên)")

                tcn_explanation = " và ".join([s.split(" \\Rightarrow ")[0] for s in tcn_str])
                tcn_lines = " và ".join([s.split(" \\Rightarrow ")[1] if " \\Rightarrow " in s else "" for s in tcn_str if " \\Rightarrow " in s])

                # Lời giải chi tiết
                loigiai = ('''Từ bảng biến thiên, ta có: \\\\
            %s là các đường tiệm cận ngang (Có %s tiệm cận ngang). \\\\
            Mặt khác: \\\\
            $\\lim\\limits_{x \\to %s^-} f(x) = +\\infty \\Rightarrow x = %s$ là đường tiệm cận đứng. \\\\
            $\\lim\\limits_{x \\to %s^-} f(x) = -\\infty \\Rightarrow x = %s$ là đường tiệm cận đứng. \\\\
            (Có 2 tiệm cận đứng). \\\\
            Vậy đồ thị hàm số có tổng cộng $%s + 2 = %s$ đường tiệm cận.''' % (
                    " ".join(tcn_str), num_tcn, 
                    str_x1, str_x1, 
                    str_x3, str_x3, 
                    num_tcn, str_tong_tc
                ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

