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


def bt_dang6_p2_b2_c1_ds10(self):
            # Khai báo biến
            # 1. Random tập A = (a1; a2]
            a1 = random.randint(-5, 0)
            a2 = a1 + random.randint(3, 5)

            # 2. Để câu (a) có điểm chung là {a2}, ta đặt b1 = a2
            b1 = a2
            b2 = b1 + random.randint(2, 4)

            # 3. Tập C = (m-k; m+k). Random bán kính k
            k = random.randint(1, 2)

            # Nội dung câu hỏi chính
            noidungcauhoi = (r"Cho các tập hợp $A=(%s;%s]$, $B=[%s;%s]$ và $C=(m-%s;m+%s)$." 
                             % (a1, a2, b1, b2, k, k))

            ######################################################################## Nhận biết ############################################
            # Câu a: Kiểm tra A giao B
            nb_da_1_d = r'\True $A \cap B = \{%s\}$' % a2
            nb_da_1_s = r'$A \cap B = \varnothing$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r"Ta có $A \cap B = (%s; %s] \cap [%s; %s] = \{%s\}$." % (a1, a2, b1, b2, a2)

            ######################################################################## Thông hiểu ############################################
            # Câu b: C con A <=> m-k >= a1 và m+k <= a2
            # m >= a1+k và m <= a2-k
            m_min_b = a1 + k
            m_max_b = a2 - k

            if m_min_b <= m_max_b:
                th_da_1_d = r'\True Điều kiện để $C \subset A$ là $%s \le m \le %s$' % (m_min_b, m_max_b)
                loigiai_th_1 = (r"Để $C \subset A$ thì $\begin{cases} m-%s \ge %s \\ m+%s \le %s \end{cases} \Leftrightarrow \begin{cases} m \ge %s \\ m \le %s \end{cases} \Leftrightarrow %s \le m \le %s$." 
                                % (k, a1, k, a2, m_min_b, m_max_b, m_min_b, m_max_b))
            else:
                th_da_1_d = r'\True Không có giá trị $m$ để $C \subset A$'
                loigiai_th_1 = r"Do độ dài tập $C$ lớn hơn tập $A$ nên không có giá trị $m$ thỏa mãn $C \subset A$."

            th_da_1_s = r'Điều kiện để $C \subset A$ là $m > %s$' % (m_max_b + 1)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            ######################################################################## Vận dụng ############################################
            # Câu c: B giao C bằng rỗng <=> m+k <= b1 hoặc m-k >= b2
            # m <= b1-k hoặc m >= b2+k
            m_left_c = b1 - k
            m_right_c = b2 + k

            vd_da_1_d = r'\True Điều kiện để $B \cap C = \varnothing$ là $m \le %s$ hoặc $m \ge %s$' % (m_left_c, m_right_c)
            vd_da_1_s = r'Điều kiện để $B \cap C = \varnothing$ là $%s < m < %s$' % (m_left_c, m_right_c)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r"Để $B \cap C = \varnothing$ thì $\left[\begin{matrix} m+%s \le %s \\ m-%s \ge %s \end{matrix}\right. \Leftrightarrow \left[\begin{matrix} m \le %s \\ m \ge %s \end{matrix}\right.$." 
                            % (k, b1, k, b2, m_left_c, m_right_c))

            ######################################################################## Vận dụng cao ############################################
            # Câu d: B \ C = rỗng <=> B con C <=> m-k < b1 và m+k > b2
            # m < b1+k và m > b2-k
            dk_tren = b1 + k
            dk_duoi = b2 - k

            # Tìm các giá trị nguyên m trong khoảng (dk_duoi, dk_tren)
            nghiem_nguyen = [i for i in range(int(dk_duoi) + 1, int(dk_tren))]
            so_luong = len(nghiem_nguyen)

            if so_luong > 0:
                vdc_da_1_d = r'\True Có %s giá trị nguyên của $m$ để $B \setminus C = \varnothing$' % so_luong
                loigiai_vdc_1 = (r"Ta có $B \setminus C = \varnothing \Leftrightarrow B \subset C \Leftrightarrow \begin{cases} m-%s < %s \\ m+%s > %s \end{cases} \Leftrightarrow %s < m < %s$. Có %s giá trị nguyên." 
                                 % (k, b1, k, b2, dk_duoi, dk_tren, so_luong))
            else:
                vdc_da_1_d = r'\True Không có giá trị nguyên nào của $m$ để $B \setminus C = \varnothing$'
                loigiai_vdc_1 = (r"Ta có $B \setminus C = \varnothing \Leftrightarrow B \subset C \Leftrightarrow \left\{\begin{matrix} m-%s < %s \\ m+%s > %s \end{matrix}\right. \Leftrightarrow %s < m < %s$. Khoảng này không chứa giá trị nguyên nào." 
                                 % ( k,b1,k,b2,dk_duoi, dk_tren))

            vdc_da_1_s = r'Có 5 giá trị nguyên của $m$ để $B \setminus C = \varnothing$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # ========================== TRỘN VÀ XUẤT KẾT QUẢ ==========================
            # (Phần này sử dụng logic giống hệt mẫu bạn đã cung cấp)
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

