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


def bt_dang52_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Các bộ cấu hình cho bài toán: (A_val, Q_opt_val)
                # Hàm lượng cầu: Q_D(P) = A_val - P/2
                # Đảm bảo phương trình đạo hàm L'(P)=0 luôn ra nghiệm nguyên đẹp
                configs = [
                    (656, 52),   # Mẫu gốc
                    (824, 54),
                    (1004, 56),
                    (1196, 58),
                    (1400, 60)
                ]

                A, Q_opt = random.choice(configs)

                # Tính toán các giá trị dựa theo hàm chi phí cố định: C(Q) = Q^3 - 77Q^2 + 1000Q + 100
                P_44 = 2 * A - 88
                P_43 = 2 * A - 86
                P_opt = 2 * A - 2 * Q_opt

                C_opt = Q_opt**3 - 77 * Q_opt**2 + 1000 * Q_opt + 100
                L_opt = P_opt * Q_opt - C_opt

                C_43 = 43**3 - 77 * 43**2 + 1000 * 43 + 100  # C(43) = -19766
                L_43 = P_43 * 43 - C_43

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (Q_opt)]
                da = random.choice(du)

                # Tạo danh sách các phương án sai (đảm bảo không trùng với đáp án đúng)
                s_list = [Q_opt - 2, 43, Q_opt + 2, 45, 50]
                s_unique = list(set([x for x in s_list if x != Q_opt]))
                random.shuffle(s_unique)

                das1 = '$%s$' % str(s_unique[0])
                das2 = '$%s$' % str(s_unique[1])
                das3 = '$%s$' % str(s_unique[2])

                # Câu hỏi
                noidungcauhoi = ('''Một nhà sản xuất độc quyền một loại bánh gia truyền để bán ra thị trường trong dịp Tết năm nay. Qua thăm dò và nghiên cứu thị trường biết lượng cầu về loại hàng này là một hàm số $Q_D(P) = %s - \\frac{P}{2}$ theo đơn giá $P$. Nếu sản xuất loại bánh này với sản lượng $Q$ thì tổng chi phí là $C(Q) = Q^3 - 77Q^2 + 1000Q + 100$. Mức sản lượng $Q$ để doanh nghiệp có lợi nhuận cao nhất sau khi bán hết loại bánh này bằng bao nhiêu?''' % (A))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Đã sửa lỗi \')
                loigiai = ('''Điều kiện: $Q \\ge 0, P \\ge 0, Q \\in \\mathbb{N}$.\\\\
            Xét phương trình $C'(Q) = 0 \\Leftrightarrow 3Q^2 - 154Q + 1000 = 0 \\Leftrightarrow Q \\approx 43,7$\\\\
            Ta thấy $C(Q)$ nghịch biến trên $[0; 43,7)$ và đồng biến trên $[43,7; +\\infty)$.\\\\
            Điều này nghĩa là nếu số sản phẩm bán ra tối ưu không vượt quá $43$ tức ta nên sản xuất $43$ sản phẩm, nếu số sản phẩm bán ra tối ưu vượt quá $43$, ta nên sản xuất số sản phẩm đó.\\\\
            Ta có: $Q_D(P) \\le 43 \\Rightarrow P \\ge %s$ và $Q_D(P) \\ge 44 \\Rightarrow P \\le %s$\\\\
            Gọi $L(P)$ là lợi nhuận khi có giá là $P$ thì ta có:\\\\
            $L(P) = \\begin{cases} P \\left( %s - \\frac{P}{2} \\right) - \\left[ \\left( %s - \\frac{P}{2} \\right)^3 - 77\\left( %s - \\frac{P}{2} \\right)^2 + 1000\\left( %s - \\frac{P}{2} \\right) + 100 \\right], P \\le %s \\\\ P \\left( %s - \\frac{P}{2} \\right) - C(43), P \\ge %s \\end{cases}$\\\\
            Khi ấy suy ra $\\max\\limits_{[0; %s]} L(P) = L(%s) = %s$ tương ứng với sản lượng $%s$ (bán ra $%s$)\\\\
            Và $\\max\\limits_{[%s; +\\infty)} L(P) = L(%s) = %s$ tương ứng với sản lượng $43$ (bán ra $43$)\\\\
            Vậy mức sản lượng cho ra lợi nhuận cao nhất là $%s$.''' 
                           % (P_43, P_44, 
                              A, A, A, A, P_44, A, P_43, 
                              P_44, P_opt, L_opt, Q_opt, Q_opt, 
                              P_43, P_43, L_43, Q_opt))
                dapan='\\shortans[0]{$%s$}\n'%(Q_opt)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

