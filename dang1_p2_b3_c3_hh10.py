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


def bt_dang1_p2_b3_c3_hh10(self):
            # Khai báo biến
            x=symbols('x')
            y=symbols('y')
            a1=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
            b1=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
            xm=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
            ym=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
            m1=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
            n1=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
            p1=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
            m2=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
            n2=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
            p2=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])

            a=2*a1
            b=2*b1
            c=-xm**2-ym**2-a*xm-b*ym

            while a**2+b**2-4*c<=0  or (m1*a1+n1*b1+p1)**2/(m1**2+n1**2)!=(a1**2+b1**2-c):
                a1=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
                b1=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
                xm=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
                ym=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
                m1=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
                m1=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
                p1=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
                m2=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
                m2=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])
                p2=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])

                a=2*a1
                b=2*b1
                c=-xm**2-ym**2-a*xm-b*ym


            dtr=a*x+b*y+c
            r=sqrt(a1**2+b1**2-c)
            dtc=m1*x+n1*y+p1
            dtkc=m2*x+n2*y+p2

            kc=abs(m1*(-a1)+n1*(-b1)+p1)/sqrt(m1**2+n1**2)

            dtt1=(xm+a1)*x+(ym+b1)*y-(xm+a1)*xm-(ym+b1)*ym

            # Tìm ước chung lớn nhất (GCD) của các hệ số
            gcd = math.gcd(math.gcd((xm+a1), (ym+b1)), -(xm+a1)*xm-(ym+b1)*ym)
            # Rút gọn các hệ số
            hs_a = (xm+a1) // gcd
            hs_b = (ym+b1) // gcd
            hs_c = (-(xm+a1)*xm-(ym+b1)*ym) // gcd
            #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            dtt = hs_a*x+hs_b*y+hs_c

            # Nội dung câu hỏi
            noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho đường tròn $(C): x^2+y^2+%s=0$.'
                            %(latex(dtr)))



            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đường tròn $(C)$ có tâm $I(%s;%s)$, bán kính là $%s$'%(latex(-a1),latex(-b1),latex(r))
            nb_da_1_s = 'Đường tròn $(C)$ có tâm $I(%s;%s)$, bán kính là $%s$'%(latex(a1),latex(b1),latex(r))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Đường tròn $(C)$ có tâm $I(%s;%s)$, bán kính là $%s$'%(latex(-a1),latex(-b1),latex(r))
            nb_da_2_s = 'Đường tròn $(C)$ có tâm $I(%s;%s)$, bán kính là $%s$'%(latex(-a1),latex(-b1),latex(r+1))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Đường tròn $(C)$ có tâm $I(%s;%s)$, bán kính là $r=\\sqrt{(%s)^2+(%s)^2-(%s)}=%s$.'%(latex(-a1),latex(-b1),latex(-a1),latex(-b1),latex(c),latex(r),)
                        )
            loigiai_nb_2 = ('Đường tròn $(C)$ có tâm $I(%s;%s)$, bán kính là $r=\\sqrt{(%s)^2+(%s)^2-(%s)}=%s$.'%(latex(-a1),latex(-b1),latex(-a1),latex(-b1),latex(c),latex(r),)
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
            th_da_1_d = '\\True Điểm $M(%s;%s)$ thuộc đường tròn $(C)$'%(latex(xm),latex(ym))
            th_da_1_s = 'Điểm $M(%s;%s)$ không thuộc đường tròn $(C)$'%(latex(xm),latex(ym))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Điểm $M(%s;%s)$ không thuộc đường tròn $(C)$'%(latex(xm),latex(ym+1))
            th_da_2_s = 'Điểm $M(%s;%s)$ thuộc đường tròn $(C)$'%(latex(xm),latex(ym+1)) 
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Thay tọa độ điểm $M$ vào phương trình đường tròn ta thấy thỏa mãn nên điểm $M(%s;%s)$ thuộc đường tròn $(C)$. '%(latex(xm),latex(ym))
                        )
            loigiai_th_2 = ('Thay tọa độ điểm $M$ vào phương trình đường tròn ta thấy không thỏa mãn nên điểm $M(%s;%s)$ không thuộc đường tròn $(C)$. '%(latex(xm),latex(ym+1))
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
            vd_da_1_d = '\\True Đường thẳng $\\Delta: %s=0$ không tiếp xúc đường tròn $(C)$'%(latex(dtc))
            vd_da_1_s = 'Đường thẳng $\\Delta: %s=0$ tiếp xúc đường tròn $(C)$'%(latex(dtc))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Đường thẳng $\\Delta: %s=0$ không tiếp xúc đường tròn $(C)$'%(latex(dtc))
            vd_da_2_s = 'Đường thẳng $\\Delta: %s=0$ tiếp xúc đường tròn $(C)$'%(latex(dtc))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]

            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta có $d(I,\\Delta)=\\dfrac{|%s\\cdot(%s)+(%s)\\cdot(%s)+%s|}{\\sqrt{(%s)^2+(%s)^2}}=%s \\ne r$.\\\\ \n'
                            'Vậy đường thẳng $\\Delta$ không tiếp xúc đường tròn $(C)$.'
                            %(latex(m1),latex(-a1),latex(n1),latex(-b1),latex(p1),latex(m1),latex(n1),latex(kc),)
                        )
            loigiai_vd_2 = ('Ta có $d(I,\\Delta)=\\dfrac{|%s\\cdot(%s)+(%s)\\cdot(%s)+%s|}{\\sqrt{(%s)^2+(%s)^2}}=%s \\ne r$.\\\\ \n'
                            'Vậy đường thẳng $\\Delta$ không tiếp xúc đường tròn $(C)$.'
                            %(latex(m1),latex(-a1),latex(n1),latex(-b1),latex(p1),latex(m1),latex(n1),latex(kc),)
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
            vdc_da_1_d = '\\True Tiếp tuyến của đường tròn $(C)$ tại điểm $G(%s;%s)$ có phương trình $%s=0$'%(latex(xm),latex(ym),latex(dtt))
            vdc_da_1_s = 'Tiếp tuyến của đường tròn $(C)$ tại điểm $G(%s;%s)$ có phương trình $%s=0$'%(latex(xm),latex(ym),latex(dtt-1))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Tiếp tuyến của đường tròn $(C)$ tại điểm $G(%s;%s)$ có phương trình $%s=0$'%(latex(xm),latex(ym),latex(dtt))
            vdc_da_2_s = 'Tiếp tuyến của đường tròn $(C)$ tại điểm $G(%s;%s)$ có phương trình $%s=0$'%(latex(xm),latex(ym),latex(dtt+1))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Tâm $I(%s;%s)$. Tiếp tuyến tại $G(%s;%s)\\in (C)$ nhận $\\vec{IG}=(%s;%s)$ làm vectơ pháp tuyến.\\\\ \n'
                            'Vậy phương trình tiếp tuyến $%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0$.'
                            %(latex(-a1),latex(-b1),latex(xm),latex(ym),latex(xm+a1),latex(ym+b1),latex(xm+a1),latex(xm),latex(ym+b1),latex(ym),latex(dtt))
                        )
            loigiai_vdc_2 = ('Tâm $I(%s;%s)$. Tiếp tuyến tại $G(%s;%s)\\in (C)$ nhận $\\vec{IG}=(%s;%s)$ làm vectơ pháp tuyến.\\\\ \n'
                            'Vậy phương trình tiếp tuyến $%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0$.'
                            %(latex(-a1),latex(-b1),latex(xm),latex(ym),latex(xm+a1),latex(ym+b1),latex(xm+a1),latex(xm),latex(ym+b1),latex(ym),latex(dtt))
                        )
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')
            return content

