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


def bt_dang47_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Để t_max là số nguyên đẹp (t = sqrt(m)), ta chọn m là số chính phương.
            m_val = random.choice([4, 9, 16]) 
            k_val = random.randint(2, 4)
            t_max_val = int(m_val**0.5)

            # Biểu thức nồng độ
            tu = k_val * t
            mau = t**2 - t + m_val
            f_t = tu / mau

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một loại thuốc được dùng cho một bệnh nhân và nồng độ thuốc trong máu của bệnh nhân được giám sát bởi bác sĩ. Biết rằng nồng độ thuốc trong máu của bệnh nhân sau khi tiêm vào cơ thể trong $t$ giờ được cho bởi công thức $c(t) = \\frac{%s}{t^2 - t + %s} \\, (mg/L)$. Xét tính đúng, sai của các khẳng định:''' 
                             % (latex(tu), latex(m_val)))

            ########################################################################
            # a) Nhận biết: Tính c(1) ############################################
            ########################################################################
            c_1_exact = f_t.subs(t, 1)
            nb_da_1_d = '\\True $c(1) = %s$' % (latex(c_1_exact))
            nb_da_1_s = '$c(1) = %s$' % (latex(Rational(k_val, m_val))) # Sai số ở mẫu
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Thay $t=1$ vào công thức ta có: $c(1) = \\frac{%s \\cdot 1}{1^2 - 1 + %s} = %s$.''' 
                            % (k_val, m_val, latex(c_1_exact)))

            ########################################################################
            # b) Thông hiểu: Giá trị không thể đạt tới ############################
            ########################################################################
            # Tính giá trị cực đại để chọn một giá trị "không thể đạt tới" (cao hơn c_max)
            c_max_exact = f_t.subs(t, t_max_val)
            unreachable_val = int(c_max_exact) + 1 

            th_da_1_d = '\\True Sau khi tiêm thuốc nồng độ thuốc trong máu của bệnh nhân không thể đạt $%s \\, (mg/L)$' % (unreachable_val)
            th_da_1_s = 'Sau khi tiêm thuốc nồng độ thuốc trong máu của bệnh nhân có thể đạt $%s \\, (mg/L)$' % (unreachable_val)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Lời giải chi tiết về phương trình vô nghiệm
            loigiai_th_1 = ('''Xét phương trình $c(t) = %s \\Leftrightarrow \\frac{%s}{t^2 - t + %s} = %s \\Leftrightarrow %s(t^2 - t + %s) = %s \\Leftrightarrow %st^2 - (%s)t + %s = 0$. \\\\
                            Phương trình này có $\\Delta = (%s)^2 - 4 \\cdot %s \\cdot %s = %s < 0$. \\\\
                            Do phương trình vô nghiệm nên nồng độ thuốc không thể đạt mức %s mg/L.''' 
                            % (unreachable_val, latex(tu), m_val, unreachable_val, unreachable_val, m_val, latex(tu), 
                               unreachable_val, unreachable_val + k_val, unreachable_val * m_val, 
                               unreachable_val + k_val, unreachable_val, unreachable_val * m_val, (unreachable_val + k_val)**2 - 4*unreachable_val**2*m_val, unreachable_val))

            ########################################################################
            # c) Vận dụng: Thời điểm nồng độ cao nhất ############################
            ########################################################################
            vd_da_1_d = '\\True Sau khi tiêm thuốc $%sh$ thì nồng độ thuốc trong máu của bệnh nhân cao nhất' % (t_max_val)
            vd_da_1_s = 'Sau khi tiêm thuốc $1h$ thì nồng độ thuốc trong máu của bệnh nhân cao nhất'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            f_prime = simplify(diff(f_t, t))
            tu_prime = f_prime.as_numer_denom()[0]
            loigiai_vd_1 = ('''Ta có $c\'(t) = \\frac{%s}{(t^2 - t + %s)^2}$. \\\\
                            $c\'(t) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow t^2 = %s \\Leftrightarrow t = %s$ (vì $t > 0$). \\\\
                            Lập bảng biến thiên, ta thấy hàm số đạt giá trị lớn nhất tại $t = %s$.''' 
                            % (latex(tu_prime), m_val, latex(tu_prime), m_val, t_max_val, t_max_val))

            ########################################################################
            # d) Vận dụng cao: Bất phương trình nồng độ ###########################
            ########################################################################
            # Chọn ngưỡng target_val phù hợp để giải (luôn nhỏ hơn c_max)
            if k_val == 3 and m_val == 4:
                target_val = Rational(9, 10)
            else:
                target_val = simplify(c_max_exact * Rational(3, 4)) # Lấy 75% giá trị cực đại cho đẹp

            # Giải BPT và xử lý lỗi IndexError bằng cách dùng Set
            sol_bpt_set = solve(f_t >= target_val, t).as_set()
            t_start = sol_bpt_set.inf
            t_end = sol_bpt_set.sup

            vdc_da_1_d = '\\True Bác sĩ cần đợi thời gian trong khung giờ $\\left[ %s; %s \\right] (h)$ để đảm bảo nồng độ không nhỏ hơn $%s \\, (mg/L)$' % (latex(t_start), latex(t_end), latex(target_val))
            vdc_da_1_s = 'Bác sĩ cần đợi thời gian trong khung giờ $\\left[ 1; %s \\right] (h)$ để đảm bảo nồng độ không nhỏ hơn $%s \\, (mg/L)$' % (latex(t_end), latex(target_val))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Để nồng độ thuốc trong máu không nhỏ hơn $%s$ mg/L, ta giải bất phương trình: \\\\
                            $c(t) \\ge %s \\Leftrightarrow \\frac{%s}{t^2 - t + %s} \\ge %s$. \\\\
                            Vì $t^2 - t + %s > 0$ với mọi $t$, quy đồng mẫu số ta được: \\\\
                            $%s \\cdot 10 \\ge 9(t^2 - t + %s)$ (Ví dụ với các hệ số tương ứng). \\\\
                            Giải bất phương trình bậc hai trên, ta thu được tập nghiệm $t \\in \\left[ %s; %s \\right]$.''' 
                            % (latex(target_val), latex(target_val), latex(tu), m_val, latex(target_val), m_val, latex(tu), m_val, latex(t_start), latex(t_end)))

            # --- TRỘN ĐÁP ÁN VÀ XUẤT NỘI DUNG ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                da_a = random.choice(list_nb_da_1)
                da_b = random.choice(list_th_da_1)
                da_c = random.choice(list_vd_da_1)
                da_d = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([da_a, da_b, da_c, da_d]) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(da_a) + '}\n'
                '{' + str(da_b) + '}\n'
                '{' + str(da_c) + '}\n'
                '{' + str(da_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

