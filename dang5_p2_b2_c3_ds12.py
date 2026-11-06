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


def bt_dang5_p2_b2_c3_ds12(self):
            # Khai báo biến
            t=symbols('t')
            k=randint(1,5)
            a1=4*k
            v1=a1*t
            t1=6*k
            s1=Rational(a1,2)*t**2

            s11=Rational(a1,2)*t1**2

            a2=-4*k
            v2=a2*t
            c2=a1*t1

            v22=a2*t+c2

            t2=-Rational(c2,a2)

            s2=Rational(a2,2)*t**2+c2*t

            s21=Rational(a2,2)*0**2+c2*0
            s22=Rational(a2,2)*t2**2+c2*t2
            s23=s22-s21


            # Nội dung câu hỏi
            noidungcauhoi = ('Một ô tô bắt đầu chuyển động nhanh dần đều với vận tốc $v_1(t)=%s$ (m/s), trong đó thời gian $t$ tính bằng giâyzz Sau khi chuyển động được $%s$ giây thì ô tô gặp chướng ngại vật và người tài xế phanh gấp, ô tô tiếp tục chuyển động chậm dần đều với vận tốc $v_2(t)$ và gia tốc $a=%s$ (m/s$^2$) cho đến khi dừng hẳnzz'
                            %(latex(v1),latex(t1),latex(a2)
                            ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Vận tốc của ô tô tại thời điểm người tài xế phanh gấp là $%s$ (m/s)' %(latex(a1*t1))
            nb_da_1_s = 'Vận tốc của ô tô tại thời điểm người tài xế phanh gấp là $%s$ (m/s)' %(latex(a1*t1-1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Vận tốc của ô tô tại thời điểm người tài xế phanh gấp là $v_1(%s)=%s$ (m/s)zz'

                    %(latex(t1),latex(a1*t1)
                    ))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Quãng đường ô tô chuyển động nhanh dần đều là $s_1=%s$ (m)' %(latex(s11))
            th_da_1_s = 'Quãng đường ô tô chuyển động nhanh dần đều là $s_1=%s$ (m)' %(latex(s11+1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Quãng đường ô tô chuyển động nhanh dần đều $s_1=\\displaystyle \\int v_1(t) \\text{d}t=\\displaystyle \\int (%s) \\text{d}t=%s+\\text{C}_1$zz \\\\ \n'
                            'Tại thời điểm $t=0$ thì $s_1(0)=0$ nên $\\text{C}_1=0$zz \\\\ \n'
                            'Vậy quãng đường ô tô chuyển động nhanh dần đều $s_1=%s$ (m)zz'

                    %(latex(v1),latex(s1),
                    latex(s11)
                    ))


            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Thời gian từ lúc ô tô giảm tốc độ cho đến khi dừng hẳn là $%s$ giây' %(latex(t2))
            vd_da_1_s = 'Thời gian từ lúc ô tô giảm tốc độ cho đến khi dừng hẳn là $%s$ giây' %(latex(t2+1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = (
                    'Ô tô chuyển động chậm dần đều với vận tốc là $v_2(t)=\\displaystyle \\int a \\text{d}t=\\displaystyle \\int (%s) \\text{d}t=%s+\\text{C}_2$zz \\\\ \n'
                    'Vận tốc của ô tô tại thời điểm bắt đầu chuyển động chậm dần là $%s$ (m/s) suy ra $\\text{C}_2=%s$zz \\\\ \n'
                    'Suy ra $v_2(t)=%s$zz \\\\ \n'
                    'Ô tô dừng hẳn khi $v_2(t)=0$ hay $t=%s$zz \\\\ \n'
                    'Vậy thời gian từ lúc ô tô giảm tốc độ cho đến khi dừng hẳn là $%s$ giâyzz'

                    %(latex(a2),latex(v2),
                    latex(a1*t1),latex(c2),
                    latex(v22),
                    latex(t2),
                    latex(t2)
                    ))


            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Tổng quãng đường ô tô chuyển động từ lúc xuất phát đến khi dừng hẳn là $%s$ (m)' %(latex(s11+s23))
            vdc_da_1_s = 'Tổng quãng đường ô tô chuyển động từ lúc xuất phát đến khi dừng hẳn là $%s$ (m)' %(latex(s11+s23+10))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Quãng đường ô tô chuyển động chậm dần đều $s_2=\\displaystyle \\int \\limits_{%s}^{%s} v_2(t) \\text{d}t=\\displaystyle \\int \\limits_{%s}^{%s} (%s) \\text{d}t=%s$zz \\\\ \n'
                            'Vậy tổng quãng đường ô tô chuyển động từ lúc xuất phát đến khi dừng hẳn là $%s+%s=%s$ (m)zz'


                    %(latex(0),latex(t2),latex(0),latex(t2),latex(v22),latex(s23),
                    latex(s11),latex(s23),latex(s11+s23)

                    ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.').replace('phtr', '\\%').replace('{\\left(', '{').replace('\\right)}', '}')
            return content

