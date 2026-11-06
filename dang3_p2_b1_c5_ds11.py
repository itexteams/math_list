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


def bt_dang3_p2_b1_c5_ds11(self):
            # Khai báo biến
            a = symbols('a')
            b = symbols('b')
            x = symbols('x')

            n=randint(2,9)
            m1=n
            m=n*m1

            k=randint(2,7)
            p=randint(4,11)
            p1=randint(1,3)
            q=p-p1
            p2=randint(4,11)
            p3=randint(1,3)
            q2=p2-p3
            while p==p1 or p2==p3 or p % q==0 or q2 %p2==0 or m%(n+1)==0:
                m1=randint(2,5)
                n=randint(2,9)
                m=n*m1

                k=randint(2,7)
                p=randint(4,11)
                p1=randint(1,3)
                q=p-p1
                p2=randint(4,11)
                p3=randint(1,3)
                q2=p2-p3
            bmu=Rational(p,q)
            bmu1=Rational(q2,p2)
            fx=m**x+n
            f0=Rational(1,n+1)
            # Nội dung câu hỏi
            noidungcauhoi = ('Cho $a>0,b>0$ và hàm số $f(x)=\\dfrac{%s^x}{%s}$. Biết $m,n$ là các số thực thỏa mãn \\\\ \n'
                            '$\\sqrt{a}\\cdot\\sqrt[%s]{a^%s\\sqrt{a}}=a^m;\\dfrac{b^{%s}\\left( b^{%s}+b^{%s}\\right)}{b^{%s}\\left( b^{%s}+b^{%s}\\right)}=b^n$.'
                            %(latex(m),latex(fx),
                            latex(2*k+1),latex(k),latex(bmu),latex(1-bmu),latex(2-bmu),latex(bmu1),latex(1-bmu1),latex(-bmu1),))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $\\displaystyle f(0)=%s$'%(latex(f0))
            nb_da_1_s = '$\\displaystyle f(0)=%s$'%(latex(f0+1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True $\\displaystyle f(0)=%s$'%(latex(f0))
            nb_da_2_s = '$\\displaystyle f(0)=%s$'%(latex(f0-1))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Ta có $f(0)=\\displaystyle\\dfrac{%s^0}{%s^0+%s}=%s$.'%(latex(m),latex(m),latex(n),latex(f0),)
                        )
            loigiai_nb_2 = ('Ta có $f(0)=\\displaystyle\\dfrac{%s^0}{%s^0+%s}=%s$.'%(latex(m),latex(m),latex(n),latex(f0),)
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $m$ không chia hết cho $2$'
            th_da_1_s = '$m$ chia hết cho $2$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $m$ không chia hết cho $3$'
            th_da_2_s = '$m$ chia hết cho $3$'
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta có $\\sqrt{a}\\cdot\\sqrt[%s]{a^%s\\sqrt{a}}=a^\\frac{1}{2}\\cdot \\sqrt[%s]{a^%s a^\\frac{1}{2}}=a^\\frac{1}{2}\\cdot \\sqrt[%s]{a^{%s+\\frac{1}{2}}}=a^\\frac{1}{2}\\cdot \\sqrt[%s]{a^{%s}}=a^\\frac{1}{2}\\cdot a^\\frac{1}{2}=a=a^m$.\\\\ \n'
                            'Vậy $m=1$ không chia hết cho $2$.'
                            %(latex(2*k+1),latex(k),latex(2*k+1),latex(k),latex(2*k+1),latex(k),latex(2*k+1),latex(Rational(2*k+1,2)),)
                        )
            loigiai_th_2 = ('Ta có $\\sqrt{a}\\cdot\\sqrt[%s]{a^%s\\sqrt{a}}=a^\\frac{1}{2}\\cdot \\sqrt[%s]{a^%s a^\\frac{1}{2}}=a^\\frac{1}{2}\\cdot \\sqrt[%s]{a^{%s+\\frac{1}{2}}}=a^\\frac{1}{2}\\cdot \\sqrt[%s]{a^{%s}}=a^\\frac{1}{2}\\cdot a^\\frac{1}{2}=a=a^m$.\\\\ \n'
                            'Vậy $m=1$ không chia hết cho $3$.'
                            %(latex(2*k+1),latex(k),latex(2*k+1),latex(k),latex(2*k+1),latex(k),latex(2*k+1),latex(Rational(2*k+1,2)),)
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $m=n$'
            vd_da_1_s = '$m>n$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True $m=n$'
            vd_da_2_s = '$m<n$'
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]

            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta có $\\dfrac{b^{%s}\\left( b^{%s}+b^{%s}\\right)}{b^{%s}\\left( b^{%s}+b^{%s}\\right)}=$'
                            '$\\dfrac{b^{%s}\\cdot b^{%s}+b^{%s}\\cdot b^{%s}}{b^{%s}\\cdot b^{%s}+b^{%s}\\cdot b^{%s}}=$'
                            '$\\dfrac{b+b^{2}}{b+1}=\\dfrac{b(1+b)}{b+1}=b=b^n$.\\\\ \n'
                            'Vậy $n=1\\Rightarrow m=n=1$.'
                            %(latex(bmu),latex(1-bmu),latex(2-bmu),latex(bmu1),latex(1-bmu1),latex(-bmu1),
                            latex(bmu),latex(1-bmu),latex(bmu),latex(2-bmu),latex(bmu1),latex(1-bmu1),latex(bmu1),latex(-bmu1),)
                        )
            loigiai_vd_2 = ('Ta có $\\dfrac{b^{%s}\\left( b^{%s}+b^{%s}\\right)}{b^{%s}\\left( b^{%s}+b^{%s}\\right)}=$'
                            '$\\dfrac{b^{%s}\\cdot b^{%s}+b^{%s}\\cdot b^{%s}}{b^{%s}\\cdot b^{%s}+b^{%s}\\cdot b^{%s}}=$'
                            '$\\dfrac{b+b^{2}}{b+1}=\\dfrac{b(1+b)}{b+1}=b=b^n$.\\\\ \n'
                            'Vậy $n=1\\Rightarrow m=n=1$.'
                            %(latex(bmu),latex(1-bmu),latex(2-bmu),latex(bmu1),latex(1-bmu1),latex(-bmu1),
                            latex(bmu),latex(1-bmu),latex(bmu),latex(2-bmu),latex(bmu1),latex(1-bmu1),latex(bmu1),latex(-bmu1),)
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Nếu $f(m-a)+f(n-b)=2$ thì $f(a^m)+f(b^n)=0$'
            vdc_da_1_s = 'Nếu $f(m-a)+f(n-b)=2$ thì $f(a^m)+f(b^n)=1$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Nếu $f(m-a)+f(n-b)=2$ thì $f(a^m)+f(b^n)=0$'
            vdc_da_2_s = 'Nếu $f(m-a)+f(n-b)=2$ thì $f(a^m)+f(b^n)=1$'
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Ta có với $m=1;n=1$\\\\ \n'
                            '$f(m-a)=f(1-a)=\\dfrac{%s^{1-a}}{%s^{1-a}+%s}=\\dfrac{%s^{1-a}%s^{a}}{\\left(%s^{1-a}+%s\\right)%s^{a}}=\\dfrac{%s}{%s+%s\\cdot %s^{a}}=\\dfrac{%s}{%s+ %s^{a}}$.\\\\ \n'
                            '$f(n-b)=f(1-b)=\\dfrac{%s^{1-b}}{%s^{1-b}+%s}=\\dfrac{%s^{1-b}%s^{b}}{\\left(%s^{1-b}+%s\\right)%s^{b}}=\\dfrac{%s}{%s+%s\\cdot %s^{b}}=\\dfrac{%s}{%s+ %s^{b}}$.\\\\ \n'
                            'Theo giả thiết $f(m-a)+f(n-b)=2 \\Rightarrow \\dfrac{%s}{%s+ %s^{a}}+\\dfrac{%s}{%s+ %s^{b}}=2$  $(1)$.\\\\ \n'
                            'Ta lại có \\\\ \n'
                            '$f(a^m)=f(a)=\\dfrac{%s^a}{%s^a+%s}=\\dfrac{%s^a+%s-%s}{%s^a+%s}=1-\\dfrac{%s}{%s^a+%s}$.\\\\ \n'
                            '$f(b^n)=f(b)=\\dfrac{%s^b}{%s^b+%s}=\\dfrac{%s^b+%s-%s}{%s^b+%s}=1-\\dfrac{%s}{%s^b+%s}$.\\\\ \n'
                            'Khi đó  $f(a^m)+f(b^n)=1-\\dfrac{%s}{%s^a+%s}+1-\\dfrac{%s}{%s^b+%s}=2-\\left(\\dfrac{%s}{%s^a+%s}+\\dfrac{%s}{%s^b+%s}\\right)$  $(2)$. \\\\ \n'
                            'Thay $(1)$ vào $(2)$ ta có $f(a^m)+f(b^n)=2-2=0$.'
                            %(latex(m),latex(m),latex(n), latex(m),latex(m),latex(m),latex(n),latex(m), latex(m),latex(m),latex(n),latex(m),latex(m1),latex(m1),latex(m),
                            latex(m),latex(m),latex(n), latex(m),latex(m),latex(m),latex(n),latex(m), latex(m),latex(m),latex(n),latex(m),latex(m1),latex(m1),latex(m),
                            latex(m1),latex(m1),latex(m),latex(m1),latex(m1),latex(m),
                            latex(m),latex(m),latex(n),latex(m),latex(n),latex(n),latex(m),latex(n), latex(n),latex(m),latex(n),
                            latex(m),latex(m),latex(n),latex(m),latex(n),latex(n),latex(m),latex(n), latex(n),latex(m),latex(n),
                            latex(n),latex(m),latex(n),latex(n),latex(m),latex(n),latex(n),latex(m),latex(n),latex(n),latex(m),latex(n),)
                        )
            loigiai_vdc_2 = ('Ta có với $m=1;n=1$\\\\ \n'
                            '$f(m-a)=f(1-a)=\\dfrac{%s^{1-a}}{%s^{1-a}+%s}=\\dfrac{%s^{1-a}%s^{a}}{\\left(%s^{1-a}+%s\\right)%s^{a}}=\\dfrac{%s}{%s+%s\\cdot %s^{a}}=\\dfrac{%s}{%s+ %s^{a}}$.\\\\ \n'
                            '$f(n-b)=f(1-b)=\\dfrac{%s^{1-b}}{%s^{1-b}+%s}=\\dfrac{%s^{1-b}%s^{b}}{\\left(%s^{1-b}+%s\\right)%s^{b}}=\\dfrac{%s}{%s+%s\\cdot %s^{b}}=\\dfrac{%s}{%s+ %s^{b}}$.\\\\ \n'
                            'Theo giả thiết $f(m-a)+f(n-b)=2 \\Rightarrow \\dfrac{%s}{%s+ %s^{a}}+\\dfrac{%s}{%s+ %s^{b}}=2$  $(1)$.\\\\ \n'
                            'Ta lại có \\\\ \n'
                            '$f(a^m)=f(a)=\\dfrac{%s^a}{%s^a+%s}=\\dfrac{%s^a+%s-%s}{%s^a+%s}=1-\\dfrac{%s}{%s^a+%s}$.\\\\ \n'
                            '$f(b^n)=f(b)=\\dfrac{%s^b}{%s^b+%s}=\\dfrac{%s^b+%s-%s}{%s^b+%s}=1-\\dfrac{%s}{%s^b+%s}$.\\\\ \n'
                            'Khi đó  $f(a^m)+f(b^n)=1-\\dfrac{%s}{%s^a+%s}+1-\\dfrac{%s}{%s^b+%s}=2-\\left(\\dfrac{%s}{%s^a+%s}+\\dfrac{%s}{%s^b+%s}\\right)$  $(2)$. \\\\ \n'
                            'Thay $(1)$ vào $(2)$ ta có $f(a^m)+f(b^n)=2-2=0$.'
                            %(latex(m),latex(m),latex(n), latex(m),latex(m),latex(m),latex(n),latex(m), latex(m),latex(m),latex(n),latex(m),latex(m1),latex(m1),latex(m),
                            latex(m),latex(m),latex(n), latex(m),latex(m),latex(m),latex(n),latex(m), latex(m),latex(m),latex(n),latex(m),latex(m1),latex(m1),latex(m),
                            latex(m1),latex(m1),latex(m),latex(m1),latex(m1),latex(m),
                            latex(m),latex(m),latex(n),latex(m),latex(n),latex(n),latex(m),latex(n), latex(n),latex(m),latex(n),
                            latex(m),latex(m),latex(n),latex(m),latex(n),latex(n),latex(m),latex(n), latex(n),latex(m),latex(n),
                            latex(n),latex(m),latex(n),latex(n),latex(m),latex(n),latex(n),latex(m),latex(n),latex(n),latex(m),latex(n),)
                        )
            loigiai_vdc_2 

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

