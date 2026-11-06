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


def bt_dang15_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, m = symbols('x m')

            # B1: Khởi tạo giá trị ngẫu nhiên cho bài toán
            # Xét bất phương trình: x^2 - 2(m + 1)x + 2m^2 - 5m + 11 < 0
            # f(x) = x^2 - 2(m+1)x + 2m^2 - 5m + 11
            a_coeff = 1
            b_param = -2*(m + 1)
            c_param = 2*m**2 - 5*m + 11

            noidungcauhoi = ('''Cho bất phương trình $x^2 - 2(m + 1)x + 2m^2 - 5m + 11 < 0$.''')

            # Tính Delta' = (m+1)^2 - (2m^2 - 5m + 11) = m^2 + 2m + 1 - 2m^2 + 5m - 11 = -m^2 + 7m - 10
            delta_prime = -m**2 + 7*m - 10

            ########################################################################
            # a) Khi m = 0
            m_val_a = 0
            f_a = x**2 - 2*(m_val_a + 1)*x + 2*m_val_a**2 - 5*m_val_a + 11
            # f_a = x^2 - 2x + 11. Delta' = 1 - 11 = -10 < 0 => Vô nghiệm.
            nb_da_1_d = '\\True Khi $m = 0$ thì bất phương trình vô nghiệm'
            nb_da_1_s = 'Khi $m = 0$ thì bất phương trình có tập nghiệm là $\\mathbb{R}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Khi $m = 0$, bất phương trình trở thành $x^2 - 2x + 11 < 0$. \\\\
                            Ta có $\\Delta' = (-1)^2 - 11 = -10 < 0$. \\\\
                            Vì $a = 1 > 0$ và $\\Delta' < 0$ nên $x^2 - 2x + 11 > 0$ với mọi $x \\in \\mathbb{R}$. \\\\
                            Vậy bất phương trình $x^2 - 2x + 11 < 0$ vô nghiệm.''')

            ########################################################################
            # b) Khi m >= 5
            # Delta' = -m^2 + 7m - 10. Nghiệm của Delta' là m=2, m=5. 
            # Delta' >= 0 khi 2 <= m <= 5.
            # Bất phương trình có nghiệm khi Delta' > 0. Vô nghiệm khi Delta' <= 0.
            # Delta' <= 0 <=> m <= 2 hoặc m >= 5.
            th_da_1_d = '\\True Khi $m \\ge 5$ bất phương trình vô nghiệm'
            th_da_1_s = 'Khi $m \\ge 5$ bất phương trình có nghiệm'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Bất phương trình vô nghiệm khi và chỉ khi $f(x) \\ge 0$ với mọi $x \\in \\mathbb{R}$. \\\\
                            Điều này tương đương với $\\Delta' \\le 0 \\Leftrightarrow -m^2 + 7m - 10 \\le 0 \\Leftrightarrow m \\in (-\\infty; 2] \\cup [5; +\\infty)$. \\\\
                            Do đó, khi $m \\ge 5$, bất phương trình vô nghiệm.''')

            ########################################################################
            # c) Khi m = 3
            m_val_c = 3
            # Delta'(3) = -9 + 21 - 10 = 2.
            # Nghiệm x = (m+1) +/- sqrt(Delta') = 4 +/- sqrt(2).
            # Vì a=1 > 0, f(x) < 0 lấy khoảng giữa hai nghiệm.
            vd_da_1_d = '\\True Khi $m = 3$ bất phương trình có nghiệm $x \\in (4 - \\sqrt{2}; 4 + \\sqrt{2})$'
            vd_da_1_s = 'Khi $m = 3$ bất phương trình có nghiệm $x \\in (-\\infty; 4 - \\sqrt{2}) \\cup (4 + \\sqrt{2}; +\\infty)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Khi $m = 3$, bất phương trình trở thành $x^2 - 8x + 14 < 0$. \\\\
                            Xét phương trình $x^2 - 8x + 14 = 0$ có $\\Delta' = 16 - 14 = 2$. \\\\
                            Phương trình có hai nghiệm phân biệt $x_1 = 4 - \\sqrt{2}, x_2 = 4 + \\sqrt{2}$. \\\\
                            Vì hệ số $a = 1 > 0$ nên tập nghiệm của bất phương trình là $(4 - \\sqrt{2}; 4 + \\sqrt{2})$.''')

            ########################################################################
            # d) Bất phương trình không thể có tập nghiệm R
            # Để tập nghiệm là R thì f(x) < 0 với mọi x. Điều này đòi hỏi a < 0.
            vdc_da_1_d = '\\True Bất phương trình không thể có tập nghiệm là $\\mathbb{R}$'
            vdc_da_1_s = 'Bất phương trình có tập nghiệm là $\\mathbb{R}$ khi $m$ đủ lớn'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Để bất phương trình $ax^2 + bx + c < 0$ có tập nghiệm là $\\mathbb{R}$ thì điều kiện cần là $a < 0$. \\\\
                             Trong trường hợp này, $a = 1 > 0$. \\\\
                             Do đó, $f(x)$ luôn cùng dấu dương với $a$ khi $x$ tiến ra vô cùng. \\\\
                             Vậy bất phương trình không thể có tập nghiệm là $\\mathbb{R}$.''')

            # --- Logic chọn đáp án Đúng/Sai ngẫu nhiên ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_da_1, th_da_1, vd_da_1, vdc_da_1]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ 
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

