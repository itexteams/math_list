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


def bt_dang3_p2_b1_c2_hh12(self):
            # Khai báo biến
            ab=randint(1,5)
            ad=randint(1,5)
            sa=randint(1,5)
            xc=ab
            yc=ad
            zc=0
            xs=0
            ys=0
            zs=sa
            xb=ab
            yb=0
            zb=0
            xd=0
            yd=ad
            zd=0
            xsc=xc-xs
            ysc=yc-ys
            zsc=zc-zs

            xbd=xd-xb
            ybd=yd-yb
            zbd=zd-zb

            x=symbols('x')
            y=symbols('y')
            z=symbols('z')
            pt=(ysc*zbd-ybd*zsc)*x+(-xsc*zbd+xbd*zsc)*y+(xsc*ybd-xbd*ysc)*z-(xsc*ybd-xbd*ysc)*zs

            kq=abs((ysc*zbd-ybd*zsc)*xb+(-xsc*zbd+xbd*zsc)*yb+(xsc*ybd-xbd*ysc)*zb-(xsc*ybd-xbd*ysc)*zs)/sqrt((ysc*zbd-ybd*zsc)**2+(-xsc*zbd+xbd*zsc)**2+(xsc*ybd-xbd*ysc)**2)
            # Nội dung câu hỏi
            noidungcauhoi = ('''\\immini{Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật và $SA$ vuông góc với đáy. Biết $AB=%s, AD=%s$ và $SA=%s$. Xét hệ trục tọa độ $Oxyz$ với $O$ trùng $A$, các tia $Ox, Oy, Oz$ lần lượt trùng với các tia $AB, AD, AS$ (như hình vẽ).)}
                            {\\scalebox{0.6}{ 
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\clip(-1.34,-1.24) rectangle (7.34,5.24);
                \\draw [line width=1.pt,dashed] (0.,0.)-- (2.,1.);
                \\draw [line width=1.pt,dashed] (2.,1.)-- (6.,1.);
                \\draw [line width=1.pt] (6.,1.)-- (4.,0.);
                \\draw [line width=1.pt] (4.,0.)-- (0.,0.);
                \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,1.)-- (2.,4.);
                \\draw [line width=1.pt] (2.,4.)-- (0.,0.);
                \\draw [line width=1.pt] (2.,4.)-- (4.,0.);
                \\draw [line width=1.pt] (2.,4.)-- (6.,1.);
                \\draw [->,line width=1.pt] (0.,0.) -- (-1.02,-0.5);
                \\draw [->,line width=1.pt] (6.,1.) -- (7.,1.);
                \\draw [->,line width=1.pt] (2.,4.) -- (2.,5.);
                \\draw (1.44,4.5) node[anchor=north west] {$S$};
                \\draw (1.4,1.6) node[anchor=north west] {$A$};
                \\draw (-0.56,0.5) node[anchor=north west] {$B$};
                \\draw (3.92,0) node[anchor=north west] {$C$};
                \\draw (5.84,1.6) node[anchor=north west] {$D$};
                \\draw (-0.86,-0.3) node[anchor=north west] {$x$};
                \\draw (6.42,1) node[anchor=north west] {$y$};
                \\draw (2,5) node[anchor=north west] {$z$};
            \\end{tikzpicture} }}'''
                            %(latex(ab),latex(ad),latex(sa)
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Tọa độ điểm $C$ là $(%s;%s;0)$' %(latex(ab),latex(ad))
            nb_da_1_s = 'Tọa độ điểm $C$ là $(%s;%s;%s)$' %(latex(ab),latex(ad),latex(sa))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Vì điểm $C$ nằm trêm mặt phẳng $(Oxy)$ nên có tọa độ là $(%s;%s;0)$.'''
                        %(latex(ab),latex(ad)))

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
            th_da_1_d = '\\True $\\left[ \\vec{SC}, \\vec{BD} \\right]=(%s;%s;%s)$' %(latex(ysc*zbd-ybd*zsc),latex(-xsc*zbd+xbd*zsc),latex(xsc*ybd-xbd*ysc))  
            th_da_1_s = '$\\left[ \\vec{SC}, \\vec{BD} \\right]=(%s;%s;%s)$' %(latex(ysc*zbd-ybd*zsc),latex(xsc*zbd-xbd*zsc),latex(xsc*ybd-xbd*ysc))   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $S(0;0;%s), B(%s;0;0), D(0;%s;0)$. \\\\
                            Suy ra $\\vec{SC}=(%s;%s;%s), \\vec{BD}=(%s;%s;%s)$. \\\\
                                Vậy $\\left[ \\vec{SC}, \\vec{BD} \\right]=(%s;%s;%s)$.'''         
                        %(latex(sa),latex(ab),latex(ad),
                        latex(xsc),latex(ysc),latex(zsc),
                        latex(xbd),latex(ybd),latex(zbd),
                        latex(ysc*zbd-ybd*zsc),latex(-xsc*zbd+xbd*zsc),latex(xsc*ybd-xbd*ysc)
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
            vd_da_1_d = '\\True Gọi $(P)$ là mặt phẳng chứa đường thẳng $SC$ và song song với đường thẳng $BD$. Phương trình mặt phẳng $(P)$ là $%s=0$' %(latex(pt))  
            vd_da_1_s = 'Gọi $(P)$ là mặt phẳng chứa đường thẳng $SC$ và song song với đường thẳng $BD$. Phương trình mặt phẳng $(P)$ là $%s=0$' %(latex(pt+1))   
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''$(P)$ là mặt phẳng chứa đường thẳng $SC$ và song song với đường thẳng $BD$ nên có vectơ pháp tuyến là $\\vec{n}=\\left[ \\vec{SC}, \\vec{BD} \\right]=(%s;%s;%s)$ và đi qua điểm $S$ nên có phương trình là \\\\
                            $(P): %s=0$''' 
                        %(latex(ysc*zbd-ybd*zsc),latex(-xsc*zbd+xbd*zsc),latex(xsc*ybd-xbd*ysc),
                        latex(pt)
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
            vdc_da_1_d = '\\True Khoảng cách giữa đường thẳng $BD$ và mặt phẳng $(P)$ bằng $%s$' %(latex(kq)) 
            vdc_da_1_s = 'Khoảng cách giữa đường thẳng $BD$ và mặt phẳng $(P)$ bằng $%s$' %(latex(kq**2)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Khoảng cách \\\\
                            $\\text{d}(BD,(P))=\\text{d}(B,(P))=\\frac{\\left| %s \\cdot (%s)+%s \\right|}{\\sqrt{%s+%s+%s}}=%s$.'''
                        %(latex(ysc*zbd-ybd*zsc),latex(xb),latex(-(xsc*ybd-xbd*ysc)*zs),
                        latex((ysc*zbd-ybd*zsc)**2),latex((-xsc*zbd+xbd*zsc)**2),latex((xsc*ybd-xbd*ysc)**2),latex(kq)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-')
            return content

